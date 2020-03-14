import sys
from googleapiclient.discovery import build

from Feynman.serialize import Pickle_serializer
from apiclient import errors


_ps = Pickle_serializer()


def main():

    creds = _ps.load('token.pickle')
    service = build('drive', 'v3', credentials=creds)

    # Call the Drive v3 API
    try:
        results = service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
    except errors.HttpError as err:
        print(err)
        sys.exit()

    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))


if __name__ == '__main__':
    main()
