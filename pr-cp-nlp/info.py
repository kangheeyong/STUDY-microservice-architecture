from dataclasses import dataclass, field
from typing import Optional

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


if __name__ == '__main__':
    a = DatasetInfo()
    breakpoint()

