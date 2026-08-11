"""
AI Integration Module for Micomp_Tech
Integrates Claude, Gemini, and ChatGPT for AI-powered learning assistance
"""

import os
from dotenv import load_dotenv

load_dotenv()

LANGUAGE_INSTRUCTIONS = {
    'en': '',
    'fr': ' Always respond in French, regardless of the language the question was asked in.',
}


class AIAssistant:
    """Main AI Assistant class that routes to different AI providers"""

    def __init__(self, provider='gemini'):
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

    def answer_question(self, question, context=None, language='en'):
        """Get answer from selected AI provider"""
        return self.client.answer_question(question, context, language)

    def explain_concept(self, concept, level='beginner', language='en'):
        """Explain a statistical concept"""
        return self.client.explain_concept(concept, level, language)

    def generate_exercise(self, topic, difficulty='medium', language='en'):
        """Generate a practice exercise"""
        return self.client.generate_exercise(topic, difficulty, language)


class ClaudeAssistant:
    """Claude AI Integration"""

    def __init__(self):
        self.api_key = os.getenv('CLAUDE_API_KEY')
        if not self.api_key or self.api_key.startswith('your_'):
            raise ValueError("CLAUDE_API_KEY not set in .env (still a placeholder)")

    def answer_question(self, question, context=None, language='en'):
        """Answer a question using Claude"""
        try:
            import anthropic

            client = anthropic.Anthropic(api_key=self.api_key)

            system_prompt = ("You are an expert statistician and data science educator. "
            "Answer questions about statistics, data collection, data processing, and data analysis. "
            "Provide clear, accurate, and educational responses suitable for learners at various levels."
            + LANGUAGE_INSTRUCTIONS.get(language, ''))

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

    def explain_concept(self, concept, level='beginner', language='en'):
        """Explain a statistical concept"""
        question = f"Explain the concept of '{concept}' at a {level} level. Include examples."
        return self.answer_question(question, language=language)

    def generate_exercise(self, topic, difficulty='medium', language='en'):
        """Generate a practice exercise"""
        question = f"Create a {difficulty} difficulty practice exercise about {topic}. Include the question and solution."
        return self.answer_question(question, language=language)


class GeminiAssistant:
    """Google Gemini AI Integration"""

    def __init__(self):
        self.api_key = os.getenv('GEMINI_API_KEY')
        if not self.api_key or self.api_key.startswith('your_'):
            raise ValueError("GEMINI_API_KEY not set in .env (still a placeholder)")

    def answer_question(self, question, context=None, language='en'):
        """Answer a question using Gemini"""
        try:
            import google.generativeai as genai

            genai.configure(api_key=self.api_key)
            model = genai.GenerativeModel('gemini-flash-latest')

            system_prompt = ("You are an expert statistician and data science educator. "
            "Answer questions about statistics, data collection, data processing, and data analysis. "
            "Provide clear, accurate, and educational responses suitable for learners at various levels."
            + LANGUAGE_INSTRUCTIONS.get(language, ''))

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

    def explain_concept(self, concept, level='beginner', language='en'):
        """Explain a statistical concept"""
        question = f"Explain the concept of '{concept}' at a {level} level. Include examples."
        return self.answer_question(question, language=language)

    def generate_exercise(self, topic, difficulty='medium', language='en'):
        """Generate a practice exercise"""
        question = f"Create a {difficulty} difficulty practice exercise about {topic}. Include the question and solution."
        return self.answer_question(question, language=language)


class OpenAIAssistant:
    """OpenAI ChatGPT Integration"""

    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        if not self.api_key or self.api_key.startswith('your_'):
            raise ValueError("OPENAI_API_KEY not set in .env (still a placeholder)")

    def answer_question(self, question, context=None, language='en'):
        """Answer a question using ChatGPT"""
        try:
            import openai

            openai.api_key = self.api_key

            system_prompt = ("You are an expert statistician and data science educator. "
            "Answer questions about statistics, data collection, data processing, and data analysis. "
            "Provide clear, accurate, and educational responses suitable for learners at various levels."
            + LANGUAGE_INSTRUCTIONS.get(language, ''))

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

    def explain_concept(self, concept, level='beginner', language='en'):
        """Explain a statistical concept"""
        question = f"Explain the concept of '{concept}' at a {level} level. Include examples."
        return self.answer_question(question, language=language)

    def generate_exercise(self, topic, difficulty='medium', language='en'):
        """Generate a practice exercise"""
        question = f"Create a {difficulty} difficulty practice exercise about {topic}. Include the question and solution."
        return self.answer_question(question, language=language)


# Utility Functions

def get_ai_response(question, provider='gemini', context=None, language='en'):
    """Get AI response from specified provider"""
    try:
        assistant = AIAssistant(provider=provider)
        return assistant.answer_question(question, context, language)
    except Exception as e:
        return {
            'error': str(e),
            'status': 'error'
        }


def explain_statistical_concept(concept, level='beginner', provider='gemini', language='en'):
    """Explain a statistical concept using AI"""
    try:
        assistant = AIAssistant(provider=provider)
        return assistant.explain_concept(concept, level, language)
    except Exception as e:
        return {
            'error': str(e),
            'status': 'error'
        }


def generate_practice_exercise(topic, difficulty='medium', provider='gemini', language='en'):
    """Generate a practice exercise using AI"""
    try:
        assistant = AIAssistant(provider=provider)
        return assistant.generate_exercise(topic, difficulty, language)
    except Exception as e:
        return {
            'error': str(e),
            'status': 'error'
        }
