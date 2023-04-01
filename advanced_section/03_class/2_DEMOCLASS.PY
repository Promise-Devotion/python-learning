class Person:

    def __init__(self, name) -> None:
        print('this is init')
        self.name = name

    @property
    def name(self):
        print("this is getter}")
        return self.__name

    @name.setter
    def name(self, name):
        print('this is setter')
        self.__name = name


p = Person('jim')

print(p.name)