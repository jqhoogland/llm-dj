from enum import Enum
import os
from typing import List, Literal
from openai import AsyncOpenAI
from llm_dj.config import Config
from pydantic import BaseModel

MODEL = os.getenv("MODEL", "gpt-4o-2024-08-06")
MAX_TOKENS = os.getenv("MAX_TOKENS", 2000)


class Suggestion(BaseModel):
    name: str
    artist: str
    type_: Literal["song", "album"]


class Suggestions(BaseModel):
    playlist_name: str
    description: str
    suggestions: List[Suggestion]


class LLMClient:

    def __init__(self):
        self.client = AsyncOpenAI(api_key=Config.LLM_API_KEY)

    async def get_music_suggestions(self, prompt):
        """Get music suggestions from the LLM.

        Args:
            prompt: The user's playlist request

        Returns:
            Suggestions object containing playlist details and song suggestions

        Raises:
            OpenAIError: If the API request fails
        """
        response = await self.client.beta.chat.completions.parse(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            messages=[{"role": "user", "content": prompt}],
            response_format=Suggestions,
        )
        return response.choices[0].message.parsed
