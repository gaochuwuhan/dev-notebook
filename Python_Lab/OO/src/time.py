import time as t

class Timer
def start(self):
    self.start=t.localtime()
    print('计时开始')
def stop(self):
    self.stop=t.localtime()
    print('计时结束')

def calc(self)