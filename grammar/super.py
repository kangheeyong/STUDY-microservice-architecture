class A:
    def __new__(cls, *args, **kwargs):
        a = super(A, cls).__new__(cls, *args, **kwargs)
        print('new A', cls, a)
        return a

    def __init__(self):

        print('생성자 A', self)


class B(A):
    def __init__(self, *args, **kwargs):
        self.a = 1
        # super(B, self).__init__()
        print('생성자 B', self)
    def temp(self):
        print('11')

class C(B):
    def __init__(self, *args, **kwargs):
        super(C, self).__init__()
        print('생성자 C', self)


class D(B):
    instance = None

    def __new__(cls, *args, **kwargs):
        print(cls)
        if D.instance is None:
            D.instance = super().__new__(cls, *args, **kwargs)
            D.instance._sealed = False
        print(D, B, cls, D.instance, 'new')
        return D.instance

    def __init__(self, *args, **kwargs):
        print(D, B, self)
        if self._sealed:
            return
        super().__init__(self, *args, **kwargs)
        self._sealed = True
        print('생성자 D', self)


if __name__ == '__main__':
    breakpoint()
