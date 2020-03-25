"""
Hello world
注释
turtle
"""

import turtle

#------------------------
# 单行注释

'''
多行注释
'''
#------------------------
# seq 分隔符
# end 结尾标志
print('hello','world',sep=', ',end='!')
print('hello world',end='!\n')

#------------------------
turtle.pensize(4)
turtle.pencolor('red')
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.mainloop()