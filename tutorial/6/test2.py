import numpy as np

from Feynman.serialize import Pickle_serializer


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
