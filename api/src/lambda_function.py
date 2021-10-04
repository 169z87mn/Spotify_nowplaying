import json
from src.spotify import Spotify

def lambda_handler(event, _context):
    token = event['queryStringParameters']['code']
    spotify = Spotify(token)
    track = spotify.get_current_track()

    tweet = f'{track.title} - {track.artist} #NowPlaying {track.url}'
    return {
        'statusCode': 200,
        'body': tweet
    }
