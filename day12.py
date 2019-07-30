'''
正则表达式
'''

import re

# ---------------------------
# 验证输入的用户名和QQ是否有效


def check_qq():
    username = input('输入用户名: ')
    qq = input('QQ: ')
    m1 = re.match(r'^[0-9a-zA-Z_]', username)
    if not m1:
        print('输入有效的用户名')
    m2 = re.match(r'^[1-9\d{4,11}]', qq)
    if not m2:
        print('输入有效QQ')


# ---------------------------
# 提取手机号
def phone():
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    mylist = re.findall(pattern, sentence)
    print(mylist)
    for temp in pattern.finditer(sentence):
        print(temp.group())
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m.pattern.search(sentence, m.end)

# ---------------------------
# 替换字符串


def sub():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹草曹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
                      '*', sentence, flags=re.IGNORECASE)
    print(purified)


# ---------------------------
# 拆分字符串
def split():
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。, .]', poem)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)


if __name__ == "__main__":
    check_qq()
    phone()
