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