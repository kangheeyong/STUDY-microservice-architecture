from src.info import DatasetInfo
from src.builder import DatasetBuilder


class sample(DatasetBuilder):
    def _info(self):
        return DatasetInfo(
            description='sample_descriptionssss',
            supervised_keys=('test in', ' test out'),
            citation='jeiger'
        )


if __name__ == '__main__':
    a = sample()
    breakpoint()
