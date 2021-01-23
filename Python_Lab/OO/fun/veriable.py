class V:
    _high=11
    __high=11.1
    high=111
    def __init__(self):
        self.__size='__size'
        # self.size=22
    @classmethod
    def fun1(cls,_v3=3):
        # v3=3
        __v4=4
        return _v3,cls.__high
    def fun2(self):
        return self.__size
    def _fun3(self):
        return self.__high

print('======单下划线变量=====',V()._high)
print('====从方法返回的、类的init双下划线属性=====',V().fun1())
print('====从sxhx方法返回的、类的双下划线属性=====',V()._fun3())
print('======init双下划线变量=====',V().__size)
print('======双下划线变量=====',V().__high)

