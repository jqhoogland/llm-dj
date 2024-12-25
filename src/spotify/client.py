import spotipy
from spotipy.oauth2 import SpotifyOAuth
from ..config import Config

class SpotifyClient:
    def __init__(self):
        self.client = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=Config.SPOTIFY_CLIENT_ID,
            client_secret=Config.SPOTIFY_CLIENT_SECRET,
            redirect_uri=Config.SPOTIFY_REDIRECT_URI,
            scope="playlist-modify-public playlist-modify-private user-library-read user-top-read"
        ))

    def create_playlist(self, name, description=""):
        user_id = self.client.current_user()["id"]
        return self.client.user_playlist_create(user_id, name, description=description)

    def search_tracks(self, query, limit=10):
        return self.client.search(query, limit=limit, type="track") 