import os
import spotipy
from spotipy import client
from api.src.track_data import Track

class Spotify():
    def __init__(self, code: str):
        self.client_id = os.getenv('SPOTIFY_CLIENT_ID')
        self.client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
        self.redirect_url = os.getenv('SPOTIFY_REDIRECT_URL')
        self.scope = os.getenv('SPOTIFY_SCOPE')

        spotify_oauth = spotipy.oauth2.SpotifyOAuth(client_id=self.client_id,
                                                    client_secret=self.client_secret,
                                                    redirect_uri=self.redirect_url,
                                                    scope=self.scope)
        token = spotify_oauth.get_access_token(code)
        self.api = spotipy.Spotify(auth=token, language='ja')

    def get_current_track(self) -> Track:
        current_track = self.api.current_user_playing_track()
        track_item = current_track['item']
        return Track(track_item['name'],
                    ', '.join([atst['name'] for atst in track_item['artists']]),
                    track_item['external_urls']['spotify'],
                    track_item['album']['name'])
