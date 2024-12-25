from typing import List, Literal, Optional
from langchain_core.language_models import BaseChatModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from pydantic import BaseModel, Field
from llm_dj.config import Config

class Suggestion(BaseModel):
    """A music suggestion."""
    name: str = Field(description="The name of the song or album")
    artist: str = Field(description="The artist name")
    type_: Literal["song", "album"] = Field(description="Whether this is a song or album suggestion")

class Suggestions(BaseModel):
    """A collection of music suggestions forming a playlist."""
    playlist_name: str = Field(description="A creative name for the playlist")
    description: str = Field(description="A brief description of the playlist's theme/mood")
    suggestions: List[Suggestion] = Field(description="List of music suggestions")

class LLMClient:
    """LLM client supporting multiple backends."""

    SUPPORTED_PROVIDERS = {
        "openai": ChatOpenAI,
        "anthropic": ChatAnthropic,
    }

    def __init__(
        self, 
        provider: str = "openai",
        model_name: Optional[str] = None,
        max_tokens: int = 2000
    ):
        """Initialize the LLM client.
        
        Args:
            provider: The LLM provider to use ("openai" or "anthropic")
            model_name: The specific model to use. If None, uses provider defaults
            max_tokens: Maximum tokens for response
        """
        if provider not in self.SUPPORTED_PROVIDERS:
            raise ValueError(f"Provider {provider} not supported. Choose from: {list(self.SUPPORTED_PROVIDERS.keys())}")

        # Set default models per provider
        default_models = {
            "openai": "gpt-4-0125-preview",
            "anthropic": "claude-3-sonnet-20240229"
        }

        model = model_name or default_models[provider]
        
        # Initialize the appropriate client
        if provider == "openai":
            self.llm: BaseChatModel = ChatOpenAI(
                api_key=Config.OPENAI_API_KEY,
                model=model,
                max_tokens=max_tokens
            )
        else:  # anthropic
            self.llm: BaseChatModel = ChatAnthropic(
                api_key=Config.ANTHROPIC_API_KEY,
                model=model,
                max_tokens=max_tokens
            )

        self.structured_llm = self.llm.with_structured_output(Suggestions)
        self.provider = provider

    async def get_music_suggestions(self, prompt: str) -> Suggestions:
        """Get music suggestions from the LLM.

        Args:
            prompt: The user's playlist request

        Returns:
            Suggestions object containing playlist details and song suggestions
        """
        return await self.structured_llm.ainvoke(prompt)
