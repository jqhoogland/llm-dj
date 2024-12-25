from anthropic import Anthropic
from ..config import Config

class LLMClient:
    def __init__(self):
        self.client = Anthropic(api_key=Config.LLM_API_KEY)

    async def get_music_suggestions(self, prompt):
        response = await self.client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=1000,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        return response.content 