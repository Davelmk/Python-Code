'''
函数、模块
'''

from random import randint


# ---------------------------
# 求阶乘
def factorial(num):
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result


m = int(input('m= '))
n = int(input('n= '))
print(factorial(m) // factorial(n) // factorial(m - n))


# ---------------------------
# 函数的参数
# 传入参数n具有默认值2
def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    return a + b + c


print(roll_dice())
print(roll_dice(3))

print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 在明确声明情况下，参数顺序可变
print(add(c=50, a=100, b=200))


# ---------------------------
# 可变参数
def addF(*args):
    total = 0
    for val in args:
        total += val
    return total


print(addF())
print(addF(1))
print(addF(1, 2))
print(addF(1, 2, 3))

# ---------------------------
# Module
# 每个文件代表一个module
# import module1 as module1
# import module2 as module2

# m1.foo()
# m2.foo()

# ---------------------------
# 如果导入的模块除了定义的函数之外还有可执行代码，
# Python解释器会在导入模块时执行这些代码
# module.py
if __name__ == "__main__":
    print('call function')
# 导入module时，print()不会执行


# ---------------------------
# 计算最大公约数和最小公倍数
def gcd(x, y):
    if x > y:
        (x, y) = (y, x)
    else:
        (x, y) = (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    return x * y // gcd(x, y)


# ---------------------------
# 回文判定
def is_palindromw(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + total % 10
        temp //= 10
    return total == num


# ---------------------------
# 素数
def is_prime(num):
    for factor in range(2,num):
        if num%factor==0:
            return False
    return True if num!=1 else False

# ---------------------------
# 变量作用域
def foo():
	b = 'hello'
    # Python中可以在函数内部再定义函数
	def bar():
        c = True
		print(a)
		print(b)
    print(c)
	bar()
    # print(c)  # NameError: name 'c' is not defined


if __name__ == '__main__':
    # 全局变量a
	a = 100
    # print(b)  # NameError: name 'b' is not defined
	foo()