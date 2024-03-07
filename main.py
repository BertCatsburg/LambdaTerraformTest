from lambda_code import lambda_handler_hello, lambda_handler_goodby, lambda_handler_skywalker
# ['queryStringParameters']['name']
import asyncio


async def main():
    # Params
    event = {
        "queryStringParameters": {
            "name": "Bert"
        }
    }

    # ***  Hello
    print('\n*** Hello ***')
    x = lambda_handler_hello(
        event=event,
        context=None,
    )
    print(x)

    # *** Goodby
    print('\n*** Goodby ***')
    y = lambda_handler_goodby(
        event=event,
        context=None,
    )
    print(y)

    # *** Get Luke Skywalker
    print('\n*** Get Luke Skywalker ***')
    eventStarWars = {
        "queryStringParameters": {
            "name": "Skywalker"
        }
    }

    z = lambda_handler_skywalker(
        event=eventStarWars,
        context=None
    )
    print(z)


if __name__ == "__main__":
    asyncio.run(main())
