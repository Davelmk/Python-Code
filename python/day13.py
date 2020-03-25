'''
多线程
'''

from random import randint
from time import time,sleep
from multiprocessing import Process
from os import getpid
from threading import Thread


def download_task(filename):
    print('start')
    time_to_download=randint(5,10)
    sleep(time_to_download)
    print('下载完成')

def download_task_1(filename):
    print('启动进程%d' %getpid())
    print('start')
    time_to_download=randint(5,10)
    sleep(time_to_download)
    print('下载完成')


# ---------------------------
# 继承Thread类
class DownloadTask(Thread):
    def __init__(self,filename):
        super().__init__()
        self._filename=filename
    
    def run(self):
        print('start')
        time_to_download=randint(5,10)
        sleep(time_to_download)
        print('花费%d秒' %time_to_download)


def main():
    # ---------------------------
    start=time()
    download_task('test.pdf')
    download_task('test.avi')
    end=time()
    print('花费:%.2f秒' %(end-start))
    # ---------------------------
    start=time()
    p1=Process(target=download_task_1,args=('test.pdf',))
    p1.start()
    p2=Process(target=download_task_1,args=('test.avi',))
    p2.start()
    # 等待进程执行结束
    p1.join()
    p2.join()
    end=time()
    print('花费:%.2f秒' %(end-start))
    # ---------------------------
    t1=DownloadTask('test.pdf')
    t1.start()
    t1.join()

    
if __name__ == "__main__":
    main()