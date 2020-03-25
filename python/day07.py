'''
字符串
常用数据结构
'''
import sys
import os
import time
import random


# ---------------------------
# 字符串
def string():
    str1 = 'hello world'
    # 字符串长度
    print(len(str1))
    # 字符串首字母大写的拷贝
    print(str1.capitalize())
    # 字符串大写的拷贝
    print(str1.upper())
    # 查找子串 find
    print(str1.find('or'))
    print(str1.find('shit'))  # -1
    # 类似find，找不到子串时异常
    print(str1.index('shit'))
    # 是否以指定字符串开头
    print(str1.startswith('he'))
    # 是否以指定字符串结尾
    print(str1.endswith('d'))
    # 将字符串以指定宽度居中，两侧填充指定字符串
    print(str1.center(50, '*'))
    # 将字符串以指定宽度靠右放置，左侧填充指定字符串
    print(str1.rjust(50, ' '))

    str2 = 'abc123456'
    # 取出指定位置字符串
    print(str2[2])
    # 字符串切片
    # string[start:stop:step]
    print(str2[2:5])  # c12
    print(str2[2:])  # c123455
    print(str2[2::2])  # c246
    print(str2[::2])  # ac246
    print(str2[::-1])  # 654321ba
    print(str2[-3:-1])  # 45
    # 字符串是否由数字组成
    print(str2.isdigit())
    # 检查字符串是否由字母组成
    print(str2.isalpha())
    # 检查字符串是否由字母和数字组成
    print(str2.isalnum())

    str3 = '  jackfrued@126.com '
    # 裁剪左右空格
    print(str3.strip())


# ---------------------------
# List 列表
def list():
    list1 = [1, 3, 4, 5, 6]
    list2 = ['jjjj'] * 5
    print(list1)
    print(list2)
    # 列表长度
    print(len(list1))
    # 索引
    print(list1[2])
    print(list1[-1])
    # 修改
    list1[2] = 100
    # 添加元素
    list1.append(200)
    list1.insert(1, 400)
    list1 += [10990, 20030]
    # 删除
    list1.remove(3)
    if 123 in list1:
        list1.remove(123)
    del list1[0]
    # 清空列表
    list1.clear()


# ---------------------------
# 列表切片
def list_operate():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    # 遍历
    for fruit in fruits:
        print(fruit.title(), end=' ')
    # 切片
    fruits2 = fruits[1:4]
    fruits3 = fruits[-3:-1]
    # 复制（创建新对象）
    fruits4 = fruits[:]
    fruits5 = fruits[::-1]


# ---------------------------
# List sort
def list_sort():
    list1 = ['orange', 'apple', 'zoo', 'blueberry']
    # 排序后返回列表是一个新的对象
    list2 = sorted(list1)
    list3 = sorted(list1, reverse=True)
    list4 = sorted(list1, key=len)
    # 在原有List上排序
    list1.sort(reverse=True)


# ---------------------------
# 生成式语法创建列表
def create_list():
    f = [x for x in range(1, 10)]
    print(f)
    f = [x + y for x in 'ABCDE' for y in '123456']
    print(f)
    f = [x**2 for x in range(1, 1000)]
    # 查看对象占用内存的字节数
    print(sys.getsizeof(f))
    print(f)
    # 创建生成式对象
    f = (x**2 for x in range(1, 1000))
    print(sys.getsizeof(f))
    print(f)
    for val in f:
        print(val)


# ---------------------------
# 元组
# 元组中元素不可修改,线程安全
# 元组在创建时间和占用空间上优于列表
def tuple():
    t = ('罗浩', 38, True, '北京')
    print(t)
    print(t[0])
    print(t[3])
    # 遍历
    for member in t:
        print(member)
    # 元组重新赋值
    # 重新引用,原来的元组被垃圾回收
    t = ('王大锤', 20, True, '云南')
    print(t)
    # 元组转化为列表
    person = list(t)
    print(person)
    # 列表修改元素
    person[0] = '李小龙'
    # 列表转为元组
    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple = turple(fruits_list)
    print(fruits_tuple)


# ---------------------------
# 集合
# 不允许有重复元素,交,差,并
def map():
    set1 = (1, 2, 3, 4, 5, 4)
    print(set1)
    print(len(set1))
    set2 = set(range(1, 10))
    print(set2)
    set1.add(4)
    set2.update([11, 12])
    print(set1)
    print(set2)
    set2.discard(5)
    # remove()如果元素不存在会引发异常
    if 4 in set2:
        set2.remove(4)
    print(set2)
    # 遍历
    for elem in set2:
        print(elem**2, end=' ')
    # 元组转换为集合
    set3 = set((1, 2, 3, 4, 4, 3))
    print(set3.pop())
    print(set3)
    # 集合运算
    print(set1 & set2)
    print(set1 | set2)
    print(set1 - set2)
    print(set1 ^ set2)
    # 子集,超集
    print(set2 <= set1)
    print(set3 <= set1)
    print(set1 >= set2)
    print(set1 >= set3)


# ---------------------------
# 字典
def dict():
    scores = {'张三': 100, '李元芳': 97, '王五': 98}
    print(scores['张三'])
    # 遍历
    for elem in scores:
        print('%s\t%d' % (elem, scores[elem]))
    # 更新字典
    scores['李元芳'] = 65
    scores['诸葛'] = 71
    scores.update(冷面=67, 哈哈怪=88)
    print(scores)
    print(scores.get('诸葛'))
    print(scores.get('诸葛', 99))
    # 删除
    print(scores.popitem())
    print(scores.pop('张三', 100))
    # 清空
    scores.clear()
    print(scores)


# ---------------------------
# 文字跑马灯
def runing_text():
    content = '北京欢迎你......'
    # 清屏
    os.system('cls')
    print(content)
    # 休眠
    time.sleep(0.2)
    content = content[1:] + content[0]


# ---------------------------
# 生成随机验证码
def generate_code(code_len=4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


# ---------------------------
# 返回列表中最大和第二大的元素
def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2
    