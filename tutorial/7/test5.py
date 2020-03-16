import io
import os
import time
import json
import socket
from collections import defaultdict

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.http import MediaIoBaseDownload

from Feynman.etc.util import get_logger
from Feynman.serialize import Pickle_serializer


# socket.setdefaulttimeout(300)


class Google_drive():
    def __init__(self):
        self.logger = get_logger()
        self._ps = Pickle_serializer()
        self.creds = self._ps.load('token.pickle')

        while True:
            try:
                self.service = build('drive', 'v3', credentials=self.creds)
                self.logger.info('Google drive access...')
                break
            except socket.timeout:
                self.logger.info('Time-out... try restart...')

    def _get_list(self):
        result = self.service.files().list(fields='*').execute()['files']
        time.sleep(.1)
        return result

    def _get_folder_id(self, folder, rlist):
        r = {dic['name']: dic for dic in rlist}
        if folder not in r:
            parants_id = '1quTKA43JyrULAZ2kZxS9sQsjfnRNiG-z'
            body = {'name': folder,
                    'parents': [parants_id],
                    'mimeType': 'application/vnd.google-apps.folder'}
            r = self.service.files().create(body=body, fields='*').execute()
            self.logger.info('Create new folder : {}({})'.format(folder, r['id']))
            time.sleep(.1)
            return r['id']
        else:
            return r[folder]['id']

    def _upload(self, folder, files, max_data=3):
        rlist = self._get_list()
        folder_id = self._get_folder_id(folder, rlist)

        rlist = [dic for dic in rlist if folder_id in dic['parents']]

        for name, path in files.items():
            body = {'name': name,
                    'parents': [folder_id]}
            media_body = MediaFileUpload(path,
                                         resumable=True)
            r = self.service.files().create(body=body, media_body=media_body).execute()
            time.sleep(.1)
            self.logger.info('Upload new filee : {}({})/{}({})'.format(folder, folder_id, name, r['id']))

            name_list = [dic for dic in rlist if name in dic['name']]
            if len(name_list) > max_data - 1:
                del_list = sorted(name_list, key=lambda x: x['createdTime'])[:-(max_data - 1)]
                for dic in del_list:
                    self.service.files().delete(fileId=dic['id']).execute()
                    self.logger.info('Delete old file : {}({})/{}({})'.format(folder, folder_id, name, dic['id']))
                    time.sleep(.1)

    def upload(self, folder, files, max_data=3):
        while True:
            try:
                self._upload(folder, files, max_data)
                break
            except socket.timeout:
                self.logger.info('Time-out... try restart...')

    def _read_info(self, path):
        info_path = os.path.join(path, 'info')
        if not os.path.exists(info_path):
            return defaultdict(str)

        with open(info_path, 'r') as f:
            info = json.load(f)
        return defaultdict(None, info)

    def _write_info(self, info, path):
        info_path = os.path.join(path, 'info')

        with open(info_path, 'w') as f:
            json.dump(info, f)

    def _download(self, folder, path):
        if not os.path.exists(path):
            os.makedirs(path)
        path = os.path.join(path, folder)
        if not os.path.exists(path):
            os.makedirs(path)

        info = self._read_info(path)

        rlist = self._get_list()
        folder_id = self._get_folder_id(folder, rlist)

        rlist = [dic for dic in rlist if folder_id in dic['parents']]

        fname = {dic['name'] for dic in rlist}
        for name in fname:
            name_list = [dic for dic in rlist if name in dic['name']]
            file_id = max(name_list, key=lambda x: x['createdTime'])['id']

            if info[name] == file_id:
                self.logger.info('{}({}) is the latest version...'.format(name, file_id))
                continue

            info[name] = file_id
            request = self.service.files().get_media(fileId=file_id)
            fh = io.FileIO(os.path.join(path, name), 'wb')
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
            self.logger.info('Download file : {}({})'.format(os.path.join(path, name), file_id))
        self._write_info(info, path)

    def download(self, folder, path):
        while True:
            try:
                self._download(folder, path)
                break
            except socket.timeout:
                self.logger.info('Time-out... try restart...')


if __name__ == '__main__':
    a = Google_drive()
    while True:
        a.download(folder='test',
                   path='tmp')
        time.sleep(30)
