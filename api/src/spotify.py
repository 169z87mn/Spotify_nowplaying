import os
import spotipy
from api.src.track_data import Track

class Spotify():
    def __init__(self, token: str):
        self.api = spotipy.Spotify(auth=token, language='ja')

    def get_current_track(self) -> Track:
        current_track = self.api.current_user_playing_track()
        track_item = current_track['item']
        return Track(track_item['name'],
                    ', '.join([atst['name'] for atst in track_item['artists']]),
                    track_item['external_urls']['spotify'],
                    track_item['album']['name'])
