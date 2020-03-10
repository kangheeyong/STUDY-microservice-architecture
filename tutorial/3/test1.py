import time
from datetime import datetime


class Timecost():
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print('start!!')
        start = datetime.now()
        self.func()
        end = datetime.now()
        print('finish!!')
        print('timecost: {}'.format(end - start))


@Timecost
def task1():
    time.sleep(3)
    print('Hello test1')

task1()
