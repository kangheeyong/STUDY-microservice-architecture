import os
import asyncio

import websockets
from slacker import Slacker

from Feynman.etc.util import Option

token = os.environ['SLACK_TOKEN']
slack = Slacker(token)

response = slack.rtm.start()
endpoint = response.body['url']
a = 1

async def execute_bot():

    while True:
        slack.chat.post_message('#test-bot', 'test {}'.format(a))
        await asyncio.sleep(60)

async def reaction_bot():
    ws = await websockets.connect(endpoint)
    while True:
        message_json = await ws.recv()
        message_json = Option(message_json)
        print(message_json)
        if message_json.text and message_json.subtype != 'bot_message':
            if '안녕' in message_json.text and '봇' in message_json.text:
                slack.chat.post_message(message_json.channel, '안녕하세요 {}'.format(a))

async def main():
    await asyncio.gather(
        execute_bot(),
        reaction_bot()
    )


asyncio.run(main())
