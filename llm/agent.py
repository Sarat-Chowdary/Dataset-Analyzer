import anthropic
from langchain_anthropic import ChatAnthropic

class DefaultLLMAgent:
    client = anthropic.Anthropic()
    
    def get_response(self, messages):
        response = self.client.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=100,
            temperature=0.1,
            system="You are a helpful messaging assistant.",
            messages=messages
            ).content
        return response
    

LLM = ChatAnthropic(
    model="claude-3-5-haiku-20241022",
    temperature=0,
    max_tokens=1000,
    timeout=None,
    max_retries=1,
    )
