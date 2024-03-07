import logging
import json
import requests


logger = logging.getLogger()
logger.setLevel(logging.INFO)


# ##################################################
# HELLO
def lambda_handler_hello(event, context):
    logging.info(event)
    name = event['queryStringParameters']['name']

    logger.info('[HELLO] - Input Parameters: %s', name)
    result = say_hello(name=name)
    response = {
        "statusCode": 200,
        "body": {
            'result': result,
            'event': json.dumps(event)
        },
    }
    logger.info('[HELLO] - Response returned: %s', response)
    return response


def say_hello(name: str) -> str:
    return f"Hello {name}"


# ##################################################
# GOODBY
def lambda_handler_goodby(event, context):
    logging.info(event)
    name = event['queryStringParameters']['name']

    logger.info('[GOODBY] - Input Parameters: %s', name)
    say_goodby(name=name)
    response = {
        "statusCode": 200,
        "body": json.dumps({
            'result': f'Goodby {name}',
            'event': event
        }),
    }
    logger.info('[GOODBY] - Response returned: %s', response)
    return response


def say_goodby(name: str) -> str:
    return f"Goodby {name}"


# ##################################################
# WHAT
def lambda_handler_what(event, context):
    logging.info(event)
    name = event['queryStringParameters']['name']

    logger.info('[WHAT] - Input Parameters: %s', name)
    say_what(name=name)
    response = {
        "statusCode": 200,
        "body": json.dumps({
            'result': f'Hey {name}, what do you want?',
            'event': event
        }),
    }
    logger.info('[WHAT] - Response returned: %s', response)
    return response


def say_what(name: str) -> str:
    return f"Goodby {name}"


# ##################################################
# GET Luke Skywalker
def lambda_handler_skywalker(event, context):
    logging.info(event)
    response = requests.get('https://swapi.dev/api/people/1')
    result = response.text
    response = {
        "statusCode": 200,
        "body": {
            "result": result,
            "event": json.dumps(event)
        },
    }
    return response
