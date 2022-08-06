class Test:

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    data = dict(
        key1="abc",
        key2="123",
    )
    for k, v in data.items():
        print(k, v)

    print('=======')

    mk = Test('mike')
    print("hasattr(mk, 'name')", hasattr(mk, 'name'))
    print("hasattr(mk, 'key')", hasattr(mk, 'key'))
