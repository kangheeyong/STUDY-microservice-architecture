import time

import asyncio

from Feynman.etc import Try_sync_access


async def test_file_read():

    while True:
        async with Try_sync_access('test1.lock'):
            print('success read -------------->.<')
            time.sleep(2)
            print('finish read')
        time.sleep(2)

if __name__ == '__main__':
    asyncio.run(test_file_read())
