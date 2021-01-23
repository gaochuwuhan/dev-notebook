class A:
    def __init__(self,name):  #实例化对象时init方法会被自动调用
        print('iam init')
        self.name=name
    def __del__(self):  #所有实例被删掉之后del方法会被自动调用
        print('iam del')
print('result--->')
a=A('bai')
# del a
print('zuihou')

