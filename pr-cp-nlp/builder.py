from dataclasses import dataclass
from typing import Union, Optional


class InvalidConfigName(ValueError):
    pass


@dataclass
class BuilderConfig:
    name: str = "default"
    version: str = "0.0.0"
    data_dir: Optional[str] = None
    data_files: Optional[Union[dict, list]] = None
    description: Optional[str] = None

    def __post_init__(self):
        invalid_windows_characters = r"<>:/\|?*"
        for invalid_char in invalid_windows_characters:
            if invalid_char in self.name:
                raise InvalidConfigName(
                    "Bad characters from black list '{}' found in '{}'.".format(invalid_windows_characters, self.name)
                )

class DatasetBuilder:
    VERSION = "0.0.0"
    BUILDER_CONFIG_CLASS = BuilderConfig
    BUILDER_CONFIGS = []
    MANUAL_DOWNLOAD_INSTRUCTIONS = None

    def __init__(self, cache_dir=None, name=None, **config_kwargs):

        config_kwargs = dict((key, value) for key, value in config_kwargs.items() if value is not None)
        self.config = self._create_builder_config(name, **config_kwargs)

    def _create_builder_config(self, name=None, **config_kwargs):
        builder_config = None

        if not builder_config:
            if name is not None:
                config_kwargs['name'] = name
            if "version" not in config_kwargs:
                config_kwargs['version'] = self.VERSION
            builder_config = self.BUILDER_CONFIG_CLASS(**config_kwargs)


        return builder_config
a = DatasetBuilder(name = '12', version='0.1.0')
breakpoint()



