import json
import os
import openai
from core.tool_manager import ToolManager
from utils.file_utils import load_project_structure, format_context
from core.memory import SessionMemory
from dotenv import load_dotenv
from utils.review_assistant import CodeReviewer
from core.debugger import CodeDebugger
from core.vcs_integration import VCSIntegration

load_dotenv()

class CodingAgent:
    def __init__(self, project_path=None):
        self.project_path = project_path or os.getcwd()
        project_structure = load_project_structure(self.project_path)
        self.context = format_context(project_structure)
        self.tool_manager = ToolManager(self.project_path)
        self.reviewer = CodeReviewer()
        self.debugger = CodeDebugger(self.project_path)
        self.vcs = VCSIntegration(self.project_path)
        self.openai_client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    def process_request(self, user_input: str, memory: SessionMemory):
        """Process user request with memory and tool manager"""
        # Handle special commands directly
        if user_input.startswith("!review"):
            return self.handle_code_review(user_input)
        elif user_input.startswith("!debug"):
            return self.handle_debug_command(user_input)
        elif user_input.startswith("!commit"):
            return self.handle_commit_command(user_input)
        
        # Prepare messages with context and memory
        messages = self._prepare_messages(user_input, memory)
        
        # First API call to determine if tool is needed
        response = self.openai_client.chat.completions.create(
            model=os.getenv("MALAZ_MODEL", "gpt-4o-mini"),
            messages=messages,
            tools=self.tool_manager.get_tool_definitions(),
            tool_choice="auto",
            max_tokens=2000
        )
        
        response_message = response.choices[0].message
        tool_calls = response_message.tool_calls
        
        # Handle tool calls
        if tool_calls:
            messages.append({
                "role": "assistant",
                "content": response_message.content,
                "tool_calls": response_message.tool_calls
            })
            
            for tool_call in tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)
                
                # Execute tool
                tool_response = self.tool_manager.execute_tool(function_name, function_args)
                
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": function_name,
                    "content": tool_response,
                })
            
            # Second call with tool responses
            second_response = self.openai_client.chat.completions.create(
                model=os.getenv("MALAZ_MODEL", "gpt-4o-mini"),
                messages=messages
            )
            final_response = second_response.choices[0].message.content
        else:
            final_response = response_message.content
        
        # Update memory and return response
        memory.add_interaction(user_input, final_response)
        return final_response
    def handle_code_review(self, command):
        """Handle code review requests"""
        parts = command.split(maxsplit=1)
        if len(parts) < 2:
            return "Please specify file path: !review path/to/file.py"
        
        file_path = parts[1].strip()
        return self.reviewer.review_file(os.path.join(self.project_path, file_path))

    def handle_debug_command(self, command):
        """Handle debugging requests"""
        parts = command.split(maxsplit=1)
        if len(parts) < 2:
            return "Please provide error trace: !debug <trace>"
        
        error_trace = parts[1].strip()
        return self.debugger.analyze_exception(error_trace)
    
    def handle_commit_command(self, command):
        """Handle commit requests"""
        parts = command.split(maxsplit=1)
        message = parts[1].strip() if len(parts) > 1 else "Auto-commit by Malaz"
        return self.vcs.commit_changes(message)
    
    def _prepare_messages(self, user_input, memory):
        """Prepare messages for OpenAI API"""

        messages = [
            {
                "role": "system",
                "content": (
                    "You are Malaz, an expert AI coding assistant. "
                    "Your role is to help with software development tasks including "
                    "code generation, debugging, refactoring, and project management. "
                    "Current project context:\n"
                    f"{self.context}\n\n"
                    "When creating or modifying files, use relative paths. "
                    "For code changes, prefer providing exact diffs when possible. "
                    "Always verify paths before file operations."
                )
            }
        ]
        
        # Add conversation history if any
        history_context = memory.get_context()
        if history_context:
            messages.append({
                "role": "system",
                "content": f"Conversation history:\n{history_context}"
            })
        
        messages.append({"role": "user", "content": user_input})
        return messages