from enum import Enum
from typing import List, Literal
from openai import AsyncOpenAI
from llm_dj.config import Config
from pydantic import BaseModel


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
        response = await self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            max_tokens=2000,
            messages=[{
                "role": "user",
                "content": prompt
            }], 
            response_format=Suggestions
        )
        return response.choices[0].message.parsed