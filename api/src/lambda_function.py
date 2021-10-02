import json
from .spotify import Spotify

def lambda_handler(event, _context):
    spotify = Spotify()
    text = spotify.get_current_track_tweet_text()

    return {
        'statusCode': 200,
        'body': text
    }
