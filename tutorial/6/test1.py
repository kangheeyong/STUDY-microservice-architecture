import _pickle
import numpy as np

from Feynman.etc import Try_sync_access
from Feynman.etc.util import get_logger


class Pickle_serializer():
    def __init__(self):
        self.logger = get_logger()

    def load(self, fname):
        with Try_sync_access(fname + '.lock'):
            with open(fname, "rb") as f:
                data = _pickle.load(f)
        self.logger.info('Pickle load : {}'.format(fname))
        return data

    def dump(self, data, fname):
        with Try_sync_access(fname + '.lock'):
            with open(fname, "wb") as f:
                _pickle.dump(data, f)
        self.logger.info('Pickle dump : {}, {}'.format(fname, type(data)))


def test():

    _ps = Pickle_serializer()
    data = dict()
    data['item_count'] = 100000
    data['user_count'] = 1000000
    data['cluster'] = 8
    data['traffic'] = 200000
    data['timing'] = 15
    data['item_idx'] = [i for i in range(data['item_count'])]
    data['user_idx'] = [u for u in range(data['user_count'])]

    data['p_item_cluster'] = np.random.dirichlet([1 for _ in range(data['cluster'])], data['item_count']).transpose()
    data['p_cluster_user'] = np.random.dirichlet([1 for _ in range(data['cluster'])], data['user_count'])
    data['p_user'] = np.random.dirichlet([1 for _ in range(data['user_count'])], 1)

    _ps.dump(data, 'test.ps')

if __name__ == '__main__':
    test()
