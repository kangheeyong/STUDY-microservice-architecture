# -*- coding: utf-8 -*-
import os
import time
import fcntl
import errno


class try_acquire_file:
    def __init__(self, fname):
        self.fname = fname
        # self.logger = Aux.get_logger(‘try_lock’)

    def __enter__(self):
        while True:
            try:
                fd = os.open(self.fname, os.O_CREAT)
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                if os.fstat(fd).st_nlink == 0:
                    os.close(fd)
                    continue
                self.fd = fd
                break
            except IOError as e:
                if e.errno != errno.EAGAIN:
                    raise
                else:
                    # self.logger.info(f'waiting to release {self.fname}')
                    os.close(fd)
                    time.sleep(1)

    def __exit__(self, *args, **kwargs):
        os.unlink(self.fname)
        fcntl.flock(self.fd, fcntl.LOCK_UN)
        os.close(self.fd)
        del self.fd
