import json


def get_headers():
    return {
        'Access-Control-Allow-Headers': 'Content-Type,Authorization,X-Amz-Date,X-API-key,X-Amz-Security-Token',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'OPTIONS,GET,POST,PUT'
    }


def create_response(status_code, body):
    return {
        'statusCode': status_code,
        'headers':  get_headers(),
        'body': json.dumps(body)
    }
