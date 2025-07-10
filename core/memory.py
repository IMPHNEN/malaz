import os
import json
from datetime import datetime

class SessionMemory:
    def __init__(self, session_id="default", max_history=20):
        self.session_id = session_id
        self.history = []
        self.max_history = max_history
        self.memory_file = "malaz_memory.json"
        self.load()
    
    def add_interaction(self, user_input: str, agent_response: str):
        timestamp = datetime.now().isoformat()
        self.history.append({
            'timestamp': timestamp,
            'user': user_input,
            'agent': agent_response
        })
        if len(self.history) > self.max_history:
            self.history.pop(0)
        self.save()
    
    def get_context(self, max_tokens=2000):
        context = ""
        token_count = 0
        
        # Iterate from latest to oldest
        for item in reversed(self.history):
            entry = f"User: {item['user']}\nAgent: {item['agent']}\n"
            entry_tokens = len(entry.split())
            
            if token_count + entry_tokens > max_tokens:
                break
                
            context = entry + context
            token_count += entry_tokens
        
        return context.strip()
    
    def save(self):
        data = {
            'session_id': self.session_id,
            'history': self.history
        }
        with open(self.memory_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load(self):
        if not os.path.exists(self.memory_file):
            return
            
        try:
            with open(self.memory_file, 'r') as f:
                data = json.load(f)
                self.session_id = data.get('session_id', self.session_id)
                self.history = data.get('history', [])
        except Exception as e:
            print(f"Error loading memory: {e}")
    
    def reset(self):
        self.history = []
        self.save()