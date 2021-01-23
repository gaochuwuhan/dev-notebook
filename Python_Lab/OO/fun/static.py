class S:
    home='shenyang'
    @staticmethod
    def funs(name):
        print('this is',name)
        print('====静态内部调用类属性====',cls.home)
        # print('====静态内部调用普通函数====',S.fun(20))
    def fun(self,age):
        print("bai's age is",age)
    @classmethod
    def func(cls,work):
        print("bai's work is",work)
        print("====在类方法中调用静态方法:====")

        #classmethod的函数可以调用类的方法和属性
        cls.funs('cls方法里调用静态方法')  #测试在cls方法里调用静态方法，可以
        print('====cls中调用类属性====\n',cls.home)

s1=S()
# print('====测试cls====')
# s1.func('类实例化后调用cls方法') #测试将类实例化后调用cls方法
# S.func('类调用cls方法') #测试直接用类调用cls方法
# print('=====测试普通函数====')
# s1.fun(18)  # 实例化的类调用带self的普通方法
print('======测试静态方法====')
S.funs('类调用静态方法')
# s1.funs('实例化的类调用静态方法')
