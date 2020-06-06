import os
import json
from dataclasses import dataclass, field
from typing import Optional

from utils.logger import get_logger

logger = get_logger()

DATASET_INFO_FILENAME = "dataset_info.json"
DATASET_INFOS_DICT_FILE_NAME = "dataset_infos.json"

@dataclass
class SupervisedKeysData:
    input: str = field(default_factory=str)
    output: str= field(default_factory=str)


@dataclass
class DatasetInfo:
    description: str = field(default_factory=str)
    citation: str = field(default_factory=str)
    homepage: str = field(default_factory=str)
    licence: str = field(default_factory=str)
    supervised_keys: Optional[SupervisedKeysData] = None

    builder_name: Optional[str] = None
    config_name: Optional[str] = None
    version: Optional[str] = None

    split: Optional[dict] = None
    download_checksums: Optional[dict] = None
    download_size: Optional[int] = None
    dataset_size: Optional[int] = None
    size_in_bytes: Optional[int] = None

    def update(self, other_dataset_info):
        self_dict = self.__dict__
        self_dict.update(
            **{k: v for k, v in other_dataset_info.__dict__.items() if v is not None}
        )

class DatasetInfosDict(dict):

    @classmethod
    def from_directory(cls, dataset_infos_dir):
        logger.info("Loading dataset infos from '{}'".format(dataset_infos_dir))
        try:
            with open(os.path.join(dataset_infos_dir, DATASET_INFOS_DICT_FILE_NAME), "r") as f:
                dataset_info_dict = {
                    config_name: DatasetInfo(**dataset_info_dict)
                    for config_name, dataset_info_dict in json.load(f).items()
                }
        except FileNotFoundError:
            logger.warning("Can't find '{}'".format(os.path.join(dataset_infos_dir, DATASET_INFOS_DICT_FILE_NAME)))
            return {}
        else:
            return cls(**dataset_info_dict)


if __name__ == '__main__':
    a = DatasetInfo()
    breakpoint()

