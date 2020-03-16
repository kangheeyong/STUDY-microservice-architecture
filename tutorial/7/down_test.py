import time

from Feynman.cloud import Google_drive

if __name__ == '__main__':
    a = Google_drive()
    while True:
        a.download(folder='test',
                   path='tmp')
        time.sleep(30)
