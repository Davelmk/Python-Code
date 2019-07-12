"""
for循环
while循环  
"""

#------------------------
# for-in循环
# range(101): 0-100
# range(1,100): 1-99
# range(1,100,2): 1-99(奇数),2是步长
sum=0
for x in range(101):
    sum+=x
print(sum)

#------------------------
# while循环
import random
answer=random.randint(1,100)
counter=0
while True:
    counter+=1
    number=int(input('输入: '))
    if number<answer:
        print('大一点')
    elif number>answer:
        print('小一点')
    else:
        print('猜对了')
        break
print('总共猜了%d次' %(counter))

#------------------------
# 素数
from math import sqrt
num=int(input('正整数: '))
end=int(sqrt(num))
is_prime=True
for x in range(2, end+1):
    if num % x==0:
        is_prime=False
        break
if is_prime and num!=1:
    print('素数')
else:
    print('不是素数')

#------------------------
# 最大公约数
# 最小公倍数
x = int(input('x = '))
y = int(input('y = '))
if x > y:
	(x, y) = (y, x)
for factor in range(x, 0, -1):
	if x % factor == 0 and y % factor == 0:
		print('%d和%d的最大公约数是%d' % (x, y, factor))
		print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
		break