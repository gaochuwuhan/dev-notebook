def wrap1(f):
    # def w1_decorator(*args, **kw):
    #     print ('Call %s() in wrap1' % f.__name__)
    #     return f(*args, **kw) #fun()
    #return w1_decorator #fun()
    return wrap1.__name__
    # print ('return w1')

 
def wrap2(f):
    def w2_decorator(*args, **kw):
        print ('Call %s() in wrap2' % f.__name__)
        return f(*args, **kw)
    return w2_decorator
    #print('return w2')
 
 
@wrap2
@wrap1
def func(a, b):
    return a * 10 + b
 
 
if __name__ == '__main__':
    print (func(5, 6))
