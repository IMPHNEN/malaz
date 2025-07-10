import os
import argparse
from rich.console import Console
from rich.syntax import Syntax
from core.agent import CodingAgent
from core.memory import SessionMemory

console = Console()

def main():
    console.print("Malaz - AI Coding Agent", style="bold green")
    parser = argparse.ArgumentParser(description='Malaz - AI Coding Agent')
    parser.add_argument('--project', type=str, default=os.getcwd(), help='Project directory')
    parser.add_argument('command', nargs='?', type=str, help='Direct command to execute')
    args = parser.parse_args()

    session_memory = SessionMemory()
    agent = CodingAgent(project_path=args.project)

    if args.command:
        # Direct command execution
        console.print(f"[bold cyan]Executing:[/] {args.command}")
        response = agent.process_request(args.command, session_memory)
        console.print(f"[bold green]\n{response}\n[/]")
        return
    
     # Interactive mode
    console.print("[bold magenta]\n✨ Welcome to Malaz AI Agent![/]")
    console.print("Type '/help' for commands, '!review <file>' for code review, '!commit' to save changes\n")
    console.print("Type '/exit' to quit\n")

    while True:
        try:
            user_input = console.input("[bold cyan]malaz> [/]")
            
            if user_input.lower() == '/exit':
                break
                
            if user_input.startswith('/'):
                handle_command(user_input, agent, session_memory)
                continue

            # Handle special commands
            if user_input.startswith('!'):
                response = agent.process_request(user_input, session_memory)
                # Format code review output
                if user_input.startswith('!review'):
                    console.print(Syntax(response, "text", theme="monokai", line_numbers=True))
                else:
                    console.print(f"[bold green]\n{response}\n[/]")
                continue
                
            # Process natural language request
            response = agent.process_request(user_input, session_memory)
            console.print(f"[bold green]\n{response}\n[/]")
            
        except KeyboardInterrupt:
            console.print("\n[bold yellow]Session interrupted. Type /exit to quit[/]")
        except Exception as e:
            console.print(f"[bold red]Error: {str(e)}[/]")

def handle_command(command: str, agent: CodingAgent, memory: SessionMemory):
    """Handle custom commands"""
    cmd_parts = command[1:].split()
    if not cmd_parts:
        return
    
    cmd = cmd_parts[0].lower()
    
    if cmd == "help":
        console.print("[bold]Available Commands:[/]")
        console.print("/help - Show this help")
        console.print("/reset - Reset session memory")
        console.print("/context - Show project context")
        console.print("/history - Show conversation history")
        console.print("/tools - List available tools")
        console.print("/state - Show current project state")
        console.print("/exit - Exit the program")
    
    elif cmd == "reset":
        memory.reset()
        console.print("[green]Session memory has been reset[/]")
    
    elif cmd == "context":
        console.print(f"[bold]Project Context:[/]\n{agent.context}")
    
    elif cmd == "history":
        console.print("[bold]Conversation History:[/]")
        for i, item in enumerate(memory.history, 1):
            console.print(f"{i}. User: {item['user']}")
            console.print(f"   Agent: {item['agent']}")
    
    elif cmd == "tools":
        console.print("[bold]Available Tools:[/]")
        for tool in agent.tool_manager.list_tools():
            console.print(f"- {tool['name']}: {tool['description']}")
    
    elif cmd == "state":
        console.print(f"[bold]Project Path:[/] {agent.project_path}")
        console.print(f"[bold]Context:[/]\n{agent.context}")
    
    else:
        console.print(f"[red]Unknown command: {cmd}[/]")

if __name__ == "__main__":
    main()