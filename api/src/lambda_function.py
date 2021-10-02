import json

def lambda_handler(event, _context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
