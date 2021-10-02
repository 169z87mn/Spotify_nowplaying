import os
import spotipy

class Spotify():
    def __init__(self):
        user_name = '169z87mn'
        self.client_id = os.getenv('SPOTIFY_CLIENT_ID')
        self.client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
        self.redirect_url = os.getenv('SPOTIFY_REDIRECT_URL')
        self.scope = os.getenv('SPOTIFY_SCOPE')
        token = spotipy.util.prompt_for_user_token(user_name, self.scope, self.client_id, self.client_secret, self.redirect_url)

        self.api = spotipy.Spotify(auth=token, language='ja')

    def get_current_track_tweet_text(self) -> str:
        current_track = self.api.current_user_playing_track()
        # print(current_track)
        playing_track = current_track['item']
        artist_name = ', '.join([atst['name'] for atst in playing_track['artists']])
        track_name = playing_track['name']
        track_url = playing_track['external_urls']['spotify']
        album_name = playing_track['album']['name']
        # print(json.dumps(playing_track, indent=4))
        tweet = f'{track_name} - {artist_name} #NowPlaying {track_url}'
        # tweet = f'{track_name} - {artist_name} ({album_name}) #NowPlaying {track_url}'
        print(tweet)
        return tweet
