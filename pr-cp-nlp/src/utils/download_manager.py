



class DownloadManager(object):

    def __init__(
        self, dataset_name=None, data_dir=None, download_config=None
    ):
        self._dataset_name = dataset_name
        self._data_dir = data_dir
        self._download_config = download_config
        self._recorded_sizes_checksums = {}

    @property
    def downloaded_size(self):
        return sum(checksums_dict['num_bytes'] for checksums_dict in self._recorded_sizes_checksums.values())


