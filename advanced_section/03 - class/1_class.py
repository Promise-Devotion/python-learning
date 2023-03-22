"""
		学习类(Classes)
	Classes provide a means of bundling data and functionality together.
Creating a new class creates a new type of object, allowing new instances of that type to be made.
Each class instance can have attributes attached to it for maintaining its state. 
Class instances can also have methods (defined by its class) for modifying its state.
"""

# class基本写法

# create a class which named Myclass,and define a function called say


# attetion, here is class not def
class Myclass:

    def __init__(self, name) -> None:
        self.name = name

    def say(self, name):
        print(self.name)


# 实例化一个对象demo
demo = Myclass('jim')
print(demo)

demo.say('hanmeimei')
