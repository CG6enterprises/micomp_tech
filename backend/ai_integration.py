"""
AI Integration Module for Micomp_Tech
Integrates Claude, Gemini, and ChatGPT for AI-powered learning assistance
"""

import os
from dotenv import load_dotenv

load_dotenv()


class AIAssistant:
    """Main AI Assistant class that routes to different AI providers"""
    
    def __init__(self, provider='claude'):
        """
        Initialize AI Assistant
        provider: 'claude', 'gemini', or 'openai'
        """
        self.provider = provider
        
        if provider == 'claude':
            self.client = ClaudeAssistant()
        elif provider == 'gemini':
            self.client = GeminiAssistant()
        elif provider == 'openai':
            self.client = OpenAIAssistant()
        else:
            raise ValueError(f"Unknown provider: {provider}")
    
    def answer_question(self, question, context=None):
        """Get answer from selected AI provider"""
        return self.client.answer_question(question, context)
    
    def explain_concept(self, concept, level='beginner'):
        """Explain a statistical concept"""
        return self.client.explain_concept(concept, level)
    
    def generate_exercise(self, topic, difficulty='medium'):
        """Generate a practice exercise"""
        return self.client.generate_exercise(topic, difficulty)


class ClaudeAssistant:
    """Claude AI Integration"""
    
    def __init__(self):
        self.api_key = os.getenv('CLAUDE_API_KEY')
        if not self.api_key:
            raise ValueError("CLAUDE_API_KEY not found in environment variables")
    
    def answer_question(self, question, context=None):
        """Answer a question using Claude"""
        try:
            import anthropic
            
            client = anthropic.Anthropic(api_key=self.api_key)
            
            system_prompt = """You are an expert statistician and data science educator. 
            Answer questions about statistics, data collection, data processing, and data analysis.
            Provide clear, accurate, and educational responses suitable for learners at various levels."""
            
            messages = []
            if context:
                messages.append({
                    "role": "user",
                    "content": f"Context: {context}\n\nQuestion: {question}"
                })
            else:
                messages.append({
                    "role": "user",
                    "content": question
                })
            
            message = client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1024,
                system=system_prompt,
                messages=messages
            )
            
            return {
                'provider': 'Claude',
                'answer': message.content[0].text,
                'status': 'success'
            }
        except Exception as e:
            return {
                'provider': 'Claude',
                'error': str(e),
                'status': 'error'
            }
    
    def explain_concept(self, concept, level='beginner'):
        """Explain a statistical concept"""
        question = f"Explain the concept of '{concept}' at a {level} level. Include examples."
        return self.answer_question(question)
    
    def generate_exercise(self, topic, difficulty='medium'):
        """Generate a practice exercise"""
        question = f"Create a {difficulty} difficulty practice exercise about {topic}. Include the question and solution."
        return self.answer_question(question)


class GeminiAssistant:
    """Google Gemini AI Integration"""
    
    def __init__(self):
        self.api_key = os.getenv('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
    
    def answer_question(self, question, context=None):
        """Answer a question using Gemini"""
        try:
            import google.generativeai as genai
            
            genai.configure(api_key=self.api_key)
            model = genai.GenerativeModel('gemini-pro')
            
            system_prompt = """You are an expert statistician and data science educator. 
            Answer questions about statistics, data collection, data processing, and data analysis.
            Provide clear, accurate, and educational responses suitable for learners at various levels."""
            
            if context:
                prompt = f"Context: {context}\n\nQuestion: {question}"
            else:
                prompt = question
            
            response = model.generate_content(f"{system_prompt}\n\n{prompt}")
            
            return {
                'provider': 'Gemini',
                'answer': response.text,
                'status': 'success'
            }
        except Exception as e:
            return {
                'provider': 'Gemini',
                'error': str(e),
                'status': 'error'
            }
    
    def explain_concept(self, concept, level='beginner'):
        """Explain a statistical concept"""
        question = f"Explain the concept of '{concept}' at a {level} level. Include examples."
        return self.answer_question(question)
    
    def generate_exercise(self, topic, difficulty='medium'):
        """Generate a practice exercise"""
        question = f"Create a {difficulty} difficulty practice exercise about {topic}. Include the question and solution."
        return self.answer_question(question)


class OpenAIAssistant:
    """OpenAI ChatGPT Integration"""
    
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
    
    def answer_question(self, question, context=None):
        """Answer a question using ChatGPT"""
        try:
            import openai
            
            openai.api_key = self.api_key
            
            system_prompt = """You are an expert statistician and data science educator. 
            Answer questions about statistics, data collection, data processing, and data analysis.
            Provide clear, accurate, and educational responses suitable for learners at various levels."""
            
            if context:
                user_prompt = f"Context: {context}\n\nQuestion: {question}"
            else:
                user_prompt = question
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7,
                max_tokens=1024
            )
            
            return {
                'provider': 'ChatGPT',
                'answer': response['choices'][0]['message']['content'],
                'status': 'success'
            }
        except Exception as e:
            return {
                'provider': 'ChatGPT',
                'error': str(e),
                'status': 'error'
            }
    
    def explain_concept(self, concept, level='beginner'):
        """Explain a statistical concept"""
        question = f"Explain the concept of '{concept}' at a {level} level. Include examples."
        return self.answer_question(question)
    
    def generate_exercise(self, topic, difficulty='medium'):
        """Generate a practice exercise"""
        question = f"Create a {difficulty} difficulty practice exercise about {topic}. Include the question and solution."
        return self.answer_question(question)


# Utility Functions

def get_ai_response(question, provider='claude', context=None):
    """Get AI response from specified provider"""
    try:
        assistant = AIAssistant(provider=provider)
        return assistant.answer_question(question, context)
    except Exception as e:
        return {
            'error': str(e),
            'status': 'error'
        }


def explain_statistical_concept(concept, level='beginner', provider='claude'):
    """Explain a statistical concept using AI"""
    try:
        assistant = AIAssistant(provider=provider)
        return assistant.explain_concept(concept, level)
    except Exception as e:
        return {
            'error': str(e),
            'status': 'error'
        }


def generate_practice_exercise(topic, difficulty='medium', provider='claude'):
    """Generate a practice exercise using AI"""
    try:
        assistant = AIAssistant(provider=provider)
        return assistant.generate_exercise(topic, difficulty)
    except Exception as e:
        return {
            'error': str(e),
            'status': 'error'
        }
