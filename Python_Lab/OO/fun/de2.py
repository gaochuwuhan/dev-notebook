def wrap1(f):
    def w1_decorator(*args, **kw):
        print ('Call %s() in wrap1' % f.__name__)
        return f(*args, **kw)
    return w1_decorator
    # return wrap1.__name__
    

 
def wrap2(f):
    def w2_decorator(*args, **kw):
        print ('Call %s() in wrap2' % f.__name__)
        return f(*args, **kw)
    # return w2_decorator
    return wrap2.__name__
 
 
@wrap2
@wrap1
def func(a, b):
    return a * 10 + b
 
 
if __name__ == '__main__':
    print (func(5, 6))