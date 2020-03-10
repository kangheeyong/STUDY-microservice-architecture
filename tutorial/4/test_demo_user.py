import time

import json
import asyncio
import websockets
from fire import Fire

from Feynman.etc.util import get_logger


class Demo_user():

    def __init__(self):
        self.logger = get_logger()
        self.url = 'ws://localhost:8000/feed'

    async def _producer(self):
        self.logger.info('Start producer...')
        while True:
            begin_t = time.time()
            # to do
            print('user producer...')
            await self.ws.send(json.dumps({'demo user': 'hi~'}))
            # finishing
            sleep_t = max(0, 60 - int(time.time() - begin_t))
            self.logger.info('Sleep {} secs before next start'.format(sleep_t))
            await asyncio.sleep(sleep_t)

    async def _consumer(self):
        self.logger.info('Start consumer...')
        while True:
            message = json.loads(await self.ws.recv())
            # to do
            print(message)
            # finishing

    async def _main(self):
        self.logger.info('Start...')
        while True:
            try:
                self.ws = await websockets.connect(self.url)
                await asyncio.gather(
                    self._producer(),
                    self._consumer()
                )
            except:
                await asyncio.sleep(15)
                self.logger.info('Restart... after {} secs'.format(15))
                continue

    def run(self):
        asyncio.run(self._main())


if __name__ == '__main__':
    Fire(Demo_user)
