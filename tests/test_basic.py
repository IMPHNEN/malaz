"""
Basic tests for Malaz AI Coding Agent
"""
import unittest
import os
import sys

# Add parent directory to path to import modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.tool_manager import ToolManager
from core.memory import SessionMemory


class TestBasicFunctionality(unittest.TestCase):
    """Test basic functionality of Malaz components"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_project_path = os.path.dirname(__file__)
        
    def test_tool_manager_initialization(self):
        """Test that ToolManager can be initialized"""
        tool_manager = ToolManager(self.test_project_path)
        self.assertIsNotNone(tool_manager)
        
    def test_tool_manager_has_tools(self):
        """Test that ToolManager has the expected tools"""
        tool_manager = ToolManager(self.test_project_path)
        tools = tool_manager.list_tools()
        self.assertIsInstance(tools, list)
        self.assertGreater(len(tools), 0)
        
        # Check for some expected tools
        expected_tools = [
            'create_file', 'modify_file', 'run_shell', 
            'search_code', 'analyze_code', 'scaffold_project'
        ]
        tool_names = [tool['function']['name'] for tool in tools]
        
        for expected_tool in expected_tools:
            self.assertIn(expected_tool, tool_names)
    
    def test_session_memory_initialization(self):
        """Test that SessionMemory can be initialized"""
        memory = SessionMemory()
        self.assertIsNotNone(memory)
        
    def test_session_memory_add_interaction(self):
        """Test adding interactions to session memory"""
        memory = SessionMemory()
        
        # Test adding interaction
        memory.add_interaction("test input", "test response")
        context = memory.get_context()
        
        self.assertIn("test input", context)
        self.assertIn("test response", context)
        
    def test_session_memory_reset(self):
        """Test resetting session memory"""
        memory = SessionMemory()
        
        # Add some interactions
        memory.add_interaction("test1", "response1")
        memory.add_interaction("test2", "response2")
        
        # Reset and check
        memory.reset()
        context = memory.get_context()
        
        self.assertEqual(context.strip(), "")
        
    def test_tool_definitions_format(self):
        """Test that tool definitions are in correct format"""
        tool_manager = ToolManager(self.test_project_path)
        definitions = tool_manager.get_tool_definitions()
        
        self.assertIsInstance(definitions, list)
        
        for tool_def in definitions:
            # Each tool should have the required structure
            self.assertIn('type', tool_def)
            self.assertEqual(tool_def['type'], 'function')
            self.assertIn('function', tool_def)
            
            function = tool_def['function']
            self.assertIn('name', function)
            self.assertIn('description', function)
            self.assertIn('parameters', function)
            
            # Parameters should have the required structure
            params = function['parameters']
            self.assertIn('type', params)
            self.assertEqual(params['type'], 'object')
            self.assertIn('properties', params)


if __name__ == '__main__':
    unittest.main() 