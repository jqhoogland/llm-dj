import spotipy
from spotipy.oauth2 import SpotifyOAuth
from llm_dj.config import Config


class SpotifyClient:
    def __init__(self):
        self.client = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=Config.SPOTIFY_CLIENT_ID,
                client_secret=Config.SPOTIFY_CLIENT_SECRET,
                redirect_uri=Config.SPOTIFY_REDIRECT_URI,
                scope="playlist-modify-public playlist-modify-private user-library-read user-top-read",
            )
        )

    def create_playlist(self, name, description=""):
        user_id = self.client.current_user()["id"]
        return self.client.user_playlist_create(user_id, name, description=description)

    def search_tracks(self, query, limit=50):
        return self.client.search(query, limit=limit, type="track")

    def search_albums(self, query, limit=50):
        return self.client.search(query, limit=limit, type="album")

    def search_tracks_by_album(self, album_id, limit=50):
        return self.client.album_tracks(album_id, limit=limit)

    def search_artists(self, query, limit=50):
        return self.client.search(query, limit=limit, type="artist")

    def get_user_playlists(self, limit=50):
        """Get the current user's playlists."""
        return self.client.current_user_playlists(limit=limit)

    def get_playlist(self, playlist_id):
        """Get a playlist by ID."""
        return self.client.playlist(playlist_id)

    def extend_playlist(self, playlist_id, track_uris):
        """Add tracks to an existing playlist."""
        return self.client.playlist_add_items(playlist_id, track_uris)
