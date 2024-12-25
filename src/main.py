from spotify.client import SpotifyClient
from llm.client import LLMClient
import asyncio

class LLMDJ:
    def __init__(self):
        self.spotify = SpotifyClient()
        self.llm = LLMClient()

    async def create_playlist_from_prompt(self, prompt, playlist_name):
        # Get song suggestions from LLM
        suggestions = await self.llm.get_music_suggestions(prompt)
        
        # Create a new playlist
        playlist = self.spotify.create_playlist(playlist_name)
        
        # Search for and add tracks
        # Note: This is a simplified version - you'll need to parse the LLM response
        # and match it with actual Spotify tracks
        for song in suggestions:
            results = self.spotify.search_tracks(song)
            if results and results['tracks']['items']:
                track_uri = results['tracks']['items'][0]['uri']
                self.spotify.client.playlist_add_items(playlist['id'], [track_uri])

        return playlist

async def main():
    dj = LLMDJ()
    await dj.create_playlist_from_prompt(
        "Create a workout playlist with upbeat rock songs from the 80s",
        "80s Workout Rock"
    )

if __name__ == "__main__":
    asyncio.run(main()) 