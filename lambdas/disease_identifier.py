import logging
from common.request_utils import create_response

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    return create_response(200, {'message': 'Success'})