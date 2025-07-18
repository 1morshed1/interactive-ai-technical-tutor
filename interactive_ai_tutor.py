#!/usr/bin/env python3
"""
Interactive AI Technical Tutor
A command-line tool for getting technical explanations from AI models
"""

import os
import sys
from typing import Dict, List, Optional, Tuple
from dotenv import load_dotenv
from IPython.display import Markdown, display
from openai import OpenAI
import ollama
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Constants
MODEL_GPT = 'gpt-4o-mini'
MODEL_LLAMA = 'llama3.2'
MODEL_CLAUDE = 'claude-3-haiku-20240307'  # If using Anthropic API

# Configuration
AVAILABLE_MODELS = {
    'gpt': {'name': MODEL_GPT, 'provider': 'openai', 'description': 'OpenAI GPT-4o Mini'},
    'llama': {'name': MODEL_LLAMA, 'provider': 'ollama', 'description': 'Llama 3.2 (Local)'},
}

class TechnicalTutor:
    """Interactive AI Technical Tutor"""
    
    def __init__(self):
        self.setup_environment()
        self.conversation_history = []
        self.current_model = 'llama'  # Default to local model
        
    def setup_environment(self):
        """Initialize environment and API clients"""
        load_dotenv()
        
        # Initialize OpenAI client
        try:
            self.openai_client = OpenAI()
            logger.info("✅ OpenAI client initialized")
        except Exception as e:
            logger.warning(f"⚠️ OpenAI client initialization failed: {e}")
            self.openai_client = None
            
        # Test Ollama connection
        try:
            ollama.list()
            logger.info("✅ Ollama connection established")
        except Exception as e:
            logger.warning(f"⚠️ Ollama connection failed: {e}")
            
    def get_system_prompt(self) -> str:
        """Get the system prompt for the AI"""
        return """You are a helpful technical tutor who specializes in explaining:
        - Python code and programming concepts
        - Software engineering principles and best practices
        - Data science techniques and methodologies
        - Large Language Models (LLMs) and AI concepts
        - Machine learning algorithms and implementations
        
        Your explanations should be:
        - Clear and detailed but not overly verbose
        - Include practical examples when helpful
        - Explain both the "what" and the "why"
        - Suitable for someone with basic programming knowledge
        - Well-structured with proper formatting
        
        If code is provided, explain it step by step and mention any best practices or potential improvements."""
        
    def display_welcome(self):
        """Display welcome message and available options"""
        welcome_text = """
# 🎓 Interactive AI Technical Tutor

Welcome! I'm here to help you understand Python code, software engineering, data science, and LLMs.

## Available Models:
"""
        for key, model in AVAILABLE_MODELS.items():
            status = "✅" if self.test_model_availability(key) else "❌"
            welcome_text += f"- **{key}**: {model['description']} {status}\n"
        
        welcome_text += f"\n**Current model**: {AVAILABLE_MODELS[self.current_model]['description']}"
        welcome_text += "\n\n**Commands**:\n- `!model <name>` - Switch model (gpt/llama)\n- `!history` - Show conversation history\n- `!clear` - Clear conversation history\n- `!save` - Save conversation to file\n- `!quit` or `!exit` - Exit the tutor\n"
        
        display(Markdown(welcome_text))
        
    def test_model_availability(self, model_key: str) -> bool:
        """Test if a model is available"""
        model_info = AVAILABLE_MODELS.get(model_key)
        if not model_info:
            return False
            
        try:
            if model_info['provider'] == 'openai':
                return self.openai_client is not None
            elif model_info['provider'] == 'ollama':
                models = ollama.list()
                return any(model_info['name'] in model['name'] for model in models['models'])
        except Exception:
            return False
        return False
        
    def get_user_input(self) -> str:
        """Get user input with proper handling"""
        try:
            print("\n" + "="*60)
            question = input("🤔 Please enter your question (or !help for commands): ").strip()
            return question
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            sys.exit(0)
        except EOFError:
            print("\n\n👋 Goodbye!")
            sys.exit(0)
            
    def handle_command(self, command: str) -> bool:
        """Handle special commands. Returns True if command was handled."""
        if not command.startswith('!'):
            return False
            
        parts = command[1:].split()
        cmd = parts[0].lower()
        
        if cmd in ['quit', 'exit']:
            print("👋 Goodbye!")
            return True
            
        elif cmd == 'help':
            help_text = """
## 📚 Available Commands:
- `!model <name>` - Switch between models (gpt/llama)
- `!history` - Show conversation history
- `!clear` - Clear conversation history
- `!save` - Save conversation to markdown file
- `!quit` or `!exit` - Exit the tutor
- `!help` - Show this help message
"""
            display(Markdown(help_text))
            
        elif cmd == 'model':
            if len(parts) > 1:
                new_model = parts[1].lower()
                if new_model in AVAILABLE_MODELS:
                    if self.test_model_availability(new_model):
                        self.current_model = new_model
                        print(f"✅ Switched to {AVAILABLE_MODELS[new_model]['description']}")
                    else:
                        print(f"❌ Model {new_model} is not available")
                else:
                    print(f"❌ Unknown model. Available: {', '.join(AVAILABLE_MODELS.keys())}")
            else:
                print(f"Current model: {AVAILABLE_MODELS[self.current_model]['description']}")
                
        elif cmd == 'history':
            if self.conversation_history:
                history_text = "## 📜 Conversation History:\n\n"
                for i, (q, _) in enumerate(self.conversation_history, 1):
                    history_text += f"**{i}.** {q[:100]}{'...' if len(q) > 100 else ''}\n"
                display(Markdown(history_text))
            else:
                print("No conversation history yet.")
                
        elif cmd == 'clear':
            self.conversation_history.clear()
            print("✅ Conversation history cleared")
            
        elif cmd == 'save':
            self.save_conversation()
            
        else:
            print(f"❌ Unknown command: {cmd}. Type !help for available commands.")
            
        return True
        
    def save_conversation(self):
        """Save conversation history to a markdown file"""
        if not self.conversation_history:
            print("No conversation to save.")
            return
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"tutor_conversation_{timestamp}.md"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"# AI Tutor Conversation - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                for i, (question, answer) in enumerate(self.conversation_history, 1):
                    f.write(f"## Question {i}\n\n{question}\n\n")
                    f.write(f"## Answer {i}\n\n{answer}\n\n")
                    f.write("---\n\n")
                    
            print(f"✅ Conversation saved to: {filename}")
            
        except Exception as e:
            print(f"❌ Error saving conversation: {e}")
            
    def ask_question(self, question: str) -> Optional[str]:
        """Send question to the selected AI model"""
        model_info = AVAILABLE_MODELS[self.current_model]
        
        messages = [
            {"role": "system", "content": self.get_system_prompt()},
            {"role": "user", "content": f"Please give a detailed explanation to the following question: {question}"}
        ]
        
        try:
            if model_info['provider'] == 'openai':
                response = self.openai_client.chat.completions.create(
                    model=model_info['name'],
                    messages=messages,
                    temperature=0.7,
                    max_tokens=2000
                )
                return response.choices[0].message.content
                
            elif model_info['provider'] == 'ollama':
                response = ollama.chat(model=model_info['name'], messages=messages)
                return response['message']['content']
                
        except Exception as e:
            logger.error(f"Error getting response from {self.current_model}: {e}")
            print(f"❌ Error: {e}")
            return None
            
    def run_interactive_session(self):
        """Run the main interactive session"""
        self.display_welcome()
        
        while True:
            try:
                question = self.get_user_input()
                
                if not question:
                    print("Please enter a question or command.")
                    continue
                    
                # Handle commands
                if self.handle_command(question):
                    if question.startswith('!quit') or question.startswith('!exit'):
                        break
                    continue
                    
                # Process question
                print(f"🤖 Thinking... (using {AVAILABLE_MODELS[self.current_model]['description']})")
                
                answer = self.ask_question(question)
                
                if answer:
                    # Display answer
                    display(Markdown(answer))
                    
                    # Store in history
                    self.conversation_history.append((question, answer))
                    
                    # Ask for follow-up
                    print("\n💡 Follow-up question, new question, or command?")
                else:
                    print("❌ Sorry, I couldn't get a response. Please try again.")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Session interrupted. Goodbye!")
                break
            except Exception as e:
                logger.error(f"Unexpected error: {e}")
                print(f"❌ An unexpected error occurred: {e}")
                
def main():
    """Main function"""
    try:
        tutor = TechnicalTutor()
        tutor.run_interactive_session()
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        print(f"❌ Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
