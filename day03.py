"""
if-else  
"""

import getpass

#------------------------
# if语句
username=input('用户名: ')
password=input('密码: ')
# username=getpass.getpass('用户名: ')
# password=getpass.getpass('密码: ')
if username=='admin' and password=='123':
    print('验证成功')
else:
    print('验证失败')

#------------------------
x = float(input('x = '))
if x > 1:
	y = 3 * x - 5
elif x >= -1:
	y = x + 2
else:
	y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))

#------------------------
value = float(input('请输入长度: '))
unit = input('请输入单位: ')
if unit == 'in' or unit == '英寸':
	print('%f英寸 = %f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
	print('%f厘米 = %f英寸' % (value, value / 2.54))
else:
	print('请输入有效的单位')

#------------------------
import math
a=float(input('a= '))
b=float(input('b= '))
c=float(input('c= '))
if a+b>c and a+c>b and b+c>a:
    print('周长:%f' %(a+b+c))
    p=(a+b+c)/2
    area=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print('面积:%f' %(area))
else:
    print('不是三角形')