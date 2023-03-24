# 创建一个父类
class Person:

    def __init__(self, name) -> None:
        self.name = name

    def say_hello(self):
        print('hello ' + self.name)


# 继承自某个类，将这个类作为参数传递给他
class Student(Person):

    def __init__(self, name, school) -> None:
        # super()方法
        super().__init__(name)
        self.school = school

    def sing_school(self):
        print('school ' + self.school)

    def say_hello(self):
        # 使用父类中的代码
        # super().say_hello()
        print('在子类中运行')


s = Student('jim', 'peigaozh')
s.sing_school()
s.say_hello()
print(f'is this is {isinstance(s, Person)}')