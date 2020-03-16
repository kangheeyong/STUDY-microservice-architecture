import time

import json
import asyncio
from fire import Fire
from sanic import Sanic

from Feynman.etc.util import get_logger


app = Sanic('Demo_app')


class Demo_app():

    def __init__(self):
        self.logger = get_logger()

    async def _task(self):
        self.logger.info('Start task...')
        while True:
            begin_t = time.time()
            # to do
            print('app task...')
            # finishing
            sleep_t = max(0, 60 - int(time.time() - begin_t))
            self.logger.info('Sleep {} secs before next start'.format(sleep_t))
            await asyncio.sleep(sleep_t)

    async def _feed(self, request, ws):
        self.logger.info('Start feed throw :{}:{}'.format(request.ip, request.port))
        while True:
            message = json.loads(await ws.recv())
            # to do
            print('get: {}'.format(message))
            await ws.send(json.dumps({'demo app': 'hello world!!!'}))
            # finishing

    def run(self):
        app.add_task(self._task)
        app.add_websocket_route(self._feed, '/feed')
        app.run(host='0.0.0.0', port=8000)


if __name__ == '__main__':
    Fire(Demo_app)
