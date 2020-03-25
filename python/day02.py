"""
变量
运算符
类型转换
类型检查 
"""

#------------------------
a=321
b=123

print(a+b)
print(a-b)
print(a*b)
# 幂
print(a**b)
print(a/b)
# 整除，向下取整
print(a//b)
print(a%b)

#------------------------
# input() 终端输入
# 类型转换
# int() 数值/字符串 --> 整数（可以指定进制）
# float() 字符串 --> 浮点数
# str() 对象 --> 字符串（可以指定编码）
# chr() 整数 --> 字符串（一个字符）
# ord() 字符串（一个整数） --> 整数
a=int(input('a= '))
b=int(input('b= '))
print('%d+%d=%d' %(a,b,a+b))

#------------------------
# type() 类型检查
a=100
b=12.333
# 虚数，j代替i
c=1+5j
d='hello'
e=True
print(type(a),type(b),type(c),type(d),type(e))

#------------------------
# 运算符
a = 5
b = 10
c = 3
d = 4
e = 5
a += b
a -= c
a *= d
a /= e
print("a = ", a)

flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1
print("flag1 = ", flag1)
print("flag2 = ", flag2)
print("flag3 = ", flag3)
print("flag4 = ", flag4)
print("flag5 = ", flag5)
print(flag1 is True)
print(flag2 is not False)

#------------------------
# 华氏温度转摄氏度
# F=1.8C+32
f=float(input('请输入华氏温度: '))
c=(f-32)/1.8
print('%.1f华氏度=%.1f摄氏度' %(f,c))

#------------------------
# 计算周长和面积
import math
radius=float(input('半径: '))
perimeter=2*radius*math.pi
area=math.pi*radius*radius
print('周长：%f,面积：%f' %(perimeter,area))

#------------------------
# 字符串
str1 = 'helloworld!'
print('字符串的长度是:', len(str1))
print('单词首字母大写: ', str1.title())
print('字符串变大写: ', str1.upper())
# str1 = str1.upper()
print('字符串是不是大写: ', str1.isupper())
print('字符串是不是以hello开头: ', str1.startswith('hello'))
print('字符串是不是以hello结尾: ', str1.endswith('hello'))
print('字符串是不是以感叹号开头: ', str1.startswith('!'))
print('字符串是不是一感叹号结尾: ', str1.endswith('!'))
str2 = '- \u9a86\u660a'
str3 = str1.title() + ' ' + str2.lower()
print(str3)