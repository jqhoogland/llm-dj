PLAYLIST_CREATION_PROMPT = """
Given the following user request, suggest a playlist of songs:
User Request: {user_request}

Please consider:
- Genre preferences
- Mood and energy level
- Similar artists and songs
- Time period preferences

Format your response as a list of songs with artists.
"""

MUSIC_ANALYSIS_PROMPT = """
Analyze the following playlist and provide insights:
Playlist: {playlist}

Consider:
- Genre distribution
- Mood progression
- Energy flow
- Potential additions or improvements
"""
