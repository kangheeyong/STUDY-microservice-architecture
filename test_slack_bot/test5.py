import os
import sys
import asyncio

import websockets
from fire import Fire
from slacker import Slacker

from Feynman.etc.util import Config, get_logger


class base():

    def __init__(self):
        self.slack = Slacker(os.environ['SLACK_TOKEN'])
        self.logger = get_logger()
        self.response = self.slack.rtm.start()
        self.endpoint = self.response.body['url']

    async def _execute_bot(self):
        self.logger.info('start execute_bot')
        while True:
            try:
                self.slack.chat.post_message('#test-bot', 'test')
                await asyncio.sleep(60)
            except:
                self.logger.warning('something is wrong...')
                break

    async def _reaction_bot(self):
        self.logger.info('start reaction_bot')
        ws = await websockets.connect(self.endpoint)
        while True:
            try:
                message_json = await ws.recv()
                self.logger.info('get message...')
                message_json = Config(message_json)
                if message_json.text and message_json.subtype != 'bot_message':
                    if '안녕' in message_json.text and '봇' in message_json.text:
                        self.slack.chat.post_message(message_json.channel, '안녕하세요')
            except:
                self.logger.warning('something is wrong...')
                break

    async def _main(self):
        self.logger.info('start process...')
        try:
            await asyncio.gather(
                self._execute_bot(),
                self._reaction_bot()
            )
        except:
            self.logger.warning('something is wrong...')
            sys.exit()

    def run(self):
        asyncio.run(self._main())


if __name__ == '__main__':
    Fire(base)
