'''
面向对象
把一组数据结构和处理它们的方法组成对象（object），
把相同行为的对象归纳为类（class），
通过类的封装（encapsulation）隐藏内部细节，
通过继承（inheritance）实现类的特化（specialization）和泛化（generalization），
通过多态（polymorphism）实现基于对象类型的动态分派。
'''
from time import sleep

# ---------------------------
# 定义类
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s学习%s' % (self.name, course_name))


def use_stu():
    stu1 = Student('张三', 20)
    stu1.study('course_name')


# ---------------------------
# 访问可见性，public、private
# 属性和方法私有，命名使用 '__' 开头
# Python并没有从语法上严格保证私有属性或方法的私密性
# 命名惯例：让属性名以单下划线开头来表示属性是受保护的
class Test:
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def use_test():
    test = Test('hello')
    # error
    test.__bar()
    # error
    print(test.__foo)
    # 私有方法、属性仍可访问
    test._Test__bar()
    print(test._Test__foo)


# ---------------------------
# 封装
class Clock(object):
    # 数字时钟
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def __str__(self):
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


def run_clock():
    clock = Clock(23, 59, 58)
    while True:
        print(clock)
        sleep(1)
        clock.run()
