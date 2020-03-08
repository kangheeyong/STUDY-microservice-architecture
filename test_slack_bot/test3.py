import os
import asyncio

import websockets
from slacker import Slacker

from Feynman.etc.util import Option

token = os.environ['SLACK_TOKEN']
slack = Slacker(token)

response = slack.rtm.start()
sock_endpoint = response.body['url']

async def execute_bot():
    ws = await websockets.connect(sock_endpoint)
    while True:
        message_json = await ws.recv()
        message_json = Option(message_json)
        print(message_json)
        if message_json.text and message_json.subtype != 'bot_message':
            if '안녕' in message_json.text and '봇' in message_json.text:
                slack.chat.post_message(message_json.channel, '안녕하세요')

asyncio.run(execute_bot())
