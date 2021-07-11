import sys

def tmp_func():
    print(sys._getframe().f_code.co_name) #打印出函数的名字

tmp_func()