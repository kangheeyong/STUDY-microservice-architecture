import time

from Feynman.cloud import Google_drive

if __name__ == '__main__':
    a = Google_drive()
    while True:
        a.upload(folder='test',
                 files={'test2.ps': '../../../test.ps',
                        'token.pickle': '../../../token.pickle'},
                 max_data=2)
        time.sleep(180)
