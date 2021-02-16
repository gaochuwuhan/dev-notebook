# '''POSITIONAL_OR_KEYWORD'''
# def func(a,b=1):
#   print(a,b)
# func(1)
# func(2,3)
# func(a=1)
# func(a=2,b=4)

# '''VAR_POSITIONAL'''
# def say_hello(*args):
#     print('hello {0}'.format(args))

# # 通过位置传值
# say_hello('jack', 'tom')

# def func_b(*args, a, b):
#     print(args, a, b)

# # 只能通过关键字传值
# func_b('test','keyonly', a=1, b=2)

'''VAR_KEYWORD'''
def func_b(**kwargs):
    print(kwargs)

# 通过关键字传值
func_b(a=1, b=2)

'''测试带*的参数'''
#发现测试结果单星号和*args参数是一样的，x代多个未知参数，参数们是一个元组
def single(*x):
    print(x)
single([1,2,3],{11,22})

#测试双星号的结果和**kwargs是一样的，y代表多个参数，参数们是字典
def double(**y):
    print(y)
dict_data={"f":11,"s":22}
double(**dict_data) #传参时要以键值对传进去