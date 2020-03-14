import io
import time

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.http import MediaIoBaseDownload

from Feynman.etc.util import get_logger
from Feynman.serialize import Pickle_serializer


class Google_drive():
    def __init__(self):
        self.logger = get_logger()
        self._ps = Pickle_serializer()
        self.creds = self._ps.load('token.pickle')
        self.service = build('drive', 'v3', credentials=self.creds)

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

    def upload(self, folder, files, max_data=3):
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

    def download(self, folder, path):
        rlist = self._get_list()
        folder_id = self._get_folder_id(folder, rlist)

        rlist = [dic for dic in rlist if folder_id in dic['parents']]

        fname = {dic['name'] for dic in rlist}
        for name in fname:
            name_list = [dic for dic in rlist if name in dic['name']]
            file_id = max(name_list, key=lambda x: x['createdTime'])['id']

            request = self.service.files().get_media(fileId=file_id)
            fh = io.FileIO('{}/{}/{}'.format(path, folder, name), 'wb')
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
            self.logger.info('Download file : {}/{}/{}({})'.format(path, folder, name, file_id))
