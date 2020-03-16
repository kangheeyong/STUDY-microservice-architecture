import os
import time
import fcntl

import asyncio

from Feynman.etc.util import get_logger


class Try_sync_access:
    def __init__(self, fname):
        self.fname = fname
        self.logger = get_logger('try_sync_access')

    async def __aenter__(self):
        while True:
            try:
                fd = os.open(self.fname, os.O_CREAT)
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                self.fd = fd
                break
            except OSError:
                os.close(fd)
                self.logger.info('Waiting to release {}'.format(self.fname))
                await asyncio.sleep(5)

    async def __aexit__(self, exc_type, exc_value, traceback):
        # fcntl.flock(self.fd, fcntl.LOCK_UN)
        os.remove(self.fname)
        os.close(self.fd)

async def test_file_read():

    while True:
        async with Try_sync_access('test1.lock'):
            print('success read -------------->.<')
            time.sleep(2)
            print('finish read')
        time.sleep(2)

if __name__ == '__main__':
    asyncio.run(test_file_read())
