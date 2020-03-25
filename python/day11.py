'''
File
Exception

r: 读取（默认）
w: 写入（会先截断之前的内容）
x: 写入，如果文件已经存在会产生异常
a: 追加
b: 二进制模式
t: 文本模式
+: 更新（读 + 写）
'''

import time
from math import sqrt
import json
import requests

# ---------------------------
# 读


def read():
    f = None
    try:
        f = open('./res/致橡树.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('文件未找到')
    except LookupError:
        print('指定了未知编码')
    except UnicodeDecodeError:
        print('解码错误')
    finally:
        if f:
            f.close()


# ---------------------------
# with 指定文件对象的上下文环境
# 离开上下文环境时自动释放文件资源
def read_with():
    try:
        with open('./res/致橡树.txt', 'r', encoding='utf-8') as f:
            print(f)
    except FileNotFoundError:
        print('文件未找到')
    except LookupError:
        print('指定了未知编码')
    except UnicodeDecodeError:
        print('解码错误')


# ---------------------------
# 逐行读取
def read_lines():
    with open('./res/致橡树.txt', mode='r', encoding='utf-8') as f:
        for line in f:
            print(line, end=' ')
            time.sleep(0.5)

    with open('./res/致橡树.txt', encoding='utf-8') as f:
        lines = f.readlines()
    print(lines)


# ---------------------------
# 1-99,100-999,999-10000之间的素数分别写入三个不同的文件
def is_prime(n):
    assert n > 0
    for factor in range(2, int(sqrt(n)+1)):
        if n % factor == 0:
            return False
    return True if n != 1 else False

def write_prime():
    filenames=('./res/a.txt', './res/b.txt', './res/c.txt')
    fs_list=[]
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number)+'\n')
                elif number < 1000:
                    fs_list[1].write(str(number)+'\n')
                else:
                    fs_list[2].write(str(number)+'\n')
    except IOError as ex:
        print(ex)
    finally:
        for fs in fs_list:
            fs.close()


# ---------------------------
# 读写二进制文件
def open_bit_file():
    try:
        with open('./res/gudio.jpg', 'rb') as fs1:
            data=fs1.read()
            print(type(data))
        with open('./res/吉多.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError:
        print('指定文件无法打开')
    except IOError:
        print('读写文件错误')


# ---------------------------
# JSON文件
# dump:将Python对象按照JSON格式序列化到文件中
# dumps:将Python对象处理成JSON格式的字符串
# load:将文件中JSON数据反序列化成对象
# loads:将字符串的内容反序列化成Python对象
def deal_json():
    mydict={
        'name':'张三',
        'age':20,
        'QQ':123882,
        'friends':['李四','王五'],
        'cars':[
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('./res/data.json','w',encoding='utf-8') as fs:
            json.dump(mydict,fs)
    except IOError:
        print('格式化失败')


def req_json():
    # request=requests.get('https://jsonplaceholder.typicode.com/photos')
    request=requests.get('https://suggest.taobao.com/sug?code=utf-8&q=%E9%9E%8B&callback=cb')
    st=str(request.text)
    l=len(st)-1
    data=json.loads(st[5:l])
    print(data)
    for news in data['result']:
        print(news[0])
    


if __name__ == "__main__":
    # read()
    # read_with()
    # read_lines()
    # write_prime()
    # open_bit_file()
    # deal_json()
    req_json()

