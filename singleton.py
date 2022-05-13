class Singleton(object):
    _instance = None

    def __new__(cls, age):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, age):
        self.age = age
        print(self.age)


if __name__ == '__main__':
    a = Singleton(3)
    b = Singleton(4)
    print(a.__dir__())
    print(id(a))
    print(id(b))
