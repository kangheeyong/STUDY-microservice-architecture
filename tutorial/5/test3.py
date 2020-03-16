import time

from Feynman.etc import Try_sync_access


def test_file_read():

    while True:
        with Try_sync_access('test1.lock'):
            print('success read -------------->.<')
            time.sleep(2)
            print('finish read')
        time.sleep(2)

if __name__ == '__main__':
    test_file_read()
