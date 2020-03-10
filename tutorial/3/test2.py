import time
from datetime import datetime


class Timecost():
    def __init__(self):
        pass

    def dump(self, func):

        def response(*args, **kwargs):
            print('start!! at dump')
            start = datetime.now()

            func(*args, **kwargs)

            end = datetime.now()
            print('finish!!')
            print('timecost: {}'.format(end - start))

        return response


a = Timecost()


@a.dump
def task1():
    time.sleep(3)
    print('Hello test1')

task1()
