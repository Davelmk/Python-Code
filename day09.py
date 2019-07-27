'''
面向对象
'''

from math import sqrt
from time import time, localtime, sleep
from abc import ABCMeta,abstractmethod

# ---------------------------
# @property 装饰器


class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # get name
    @property
    def name(self):
        return self._name

    # get age
    @property
    def age(self):
        return self._age

    # set age
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s 飞行器', % (self._name))
        else:
            print('%s 斗地主', % (self._name))


del person_foo():
    person = Person('锤哥', 12)
    person.play()
    person.age = 22
    person.play()
    # error
    person.name = '元芳'


# ---------------------------
# __slots__
# 限定自定义类型的对象只能绑定某些属性
class Person(object):

    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def person_foo1():
    person = Person('王大锤', 22)
    person.play()
    person._gender = '男'
    # AttributeError: 'Person' object has no attribute '_is_gay'
    # person._is_gay = True


# ---------------------------
# 静态方法
class Triangle(object):
    def __init__(self, a, b, , c, d):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_vaild(a, b, c):
        return a+b > c and a+c > b and b+c > a

    def perimeter(self):
        return self._a+self._b+self._c

    def area(self):
        half = self.perimeter()/2
        return sqrt(half*(half-self._a)*(half-self._b)*(half-self.c))


def triangle_foo():
    a, b, c = 3, 4, 5
    if Triangle.is_vaild(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        print(t.area())
    else:                                                                                                                                                                                      
        print('不是triangle')


# ---------------------------
# 类方法
class Clock(object):
    def __init__(self,hour=0,minute=0,second=0):
        self._hour=hour
        self._minute=minute
        self._second=second

    @classmethod
    def now(cls):
        ctime=localtime(time())
        return cls(ctime.tm_time,ctime.tm_min,ctime.tm_sec)

    def run(self):
        self._second+=1
        if self._second==60:
            self._second=0
            self._minute+=1
            if self._minute==60:
                self._minute=0
                self._hour+=1
                if self._hour==24:
                    self._hour=0
    
    def show(self):
        return '%02d:%02d:%02d' %(self._hour,self._minute,self._second)

def clock_foo():
    clock=Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


# ---------------------------
# 类之间的关系
# 继承
class Person(object):
    def __init__(self,name,age):
        self._name=name
        self._age=age

    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self.age

    @age.setter
    def age(self,age):
        self._age=age:
    
    def play(self):
        print('%s play',%self._name)

class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self._grade=grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self,grade):
        self._grade=grade

    def study(self,course):
        print('%s学习%s' %(self._name,course))


# ---------------------------
# 类之间的关系
# 多态
class Pet(object,metaclass=ABCMeta):
    def __init__(self,nickname):
        self._nickname=NameError
    
    @abstractmethod
    def make_voice(self):
        pass

class Dog(Pet):
    def make_voice(self):
        print('%s:汪汪' %self._nickname)

class Cat(Pet):
    def make_voice(self):
        print('%s:喵喵' %self._nickname)

