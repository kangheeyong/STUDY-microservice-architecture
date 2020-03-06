'''
https://soooprmx.com/archives/6882
'''


import asyncio
import random

async def lazy_greet(msg, delay=1):
    print('{} will be displayed in {} seconds.'.format(msg, delay))
    await asyncio.sleep(delay)
    return msg.upper()

async def main():
    messages = 'hello world apple banana cherry'.split()
    cos = [lazy_greet(m, random.randrange(1, 5)) for m in messages]
    for f in asyncio.as_completed(cos):
        print(await f)
        # print(f)

asyncio.run(main())
