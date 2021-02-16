# from A1 import *  #从A1文件中倒入所有方法和变量
# ''' import A1 '''#只倒入A1模块，此时此文件中引用里面的方法会报错
# ''' from A1 import b1,B ''' #从A1文件中倒入b1,A1中的东西只有b1和B可以在这里使用
# def usea1():
#     print(isinstance(b1,B))
# usea1()
from B import B1
B1.result()
# class P1:
#     #name='long'
#     def __init__(self):
#         self.location='SH'
#         self.area='songjiang'

#     def FA(self):
#         print(1)
# class C1(P1):
#    # name='bai'
#     def __init__(self):  
#         self.location='SY'
#         self.area='dadong'   #定义了两个子类的初始化实例的属性
#         '''
#         如果想让子类继承父类的某个方法，就在子类的init函数中，调用父类的方法，如下
#         '''
#         #方法一：写出具体想要调用父类的方法  父类.方法名
#         P1.__init__(self)   #定义C1子类自己的初始化init方法调用父类的init方法：实例化的子类对象传给self
#         P1.FA(self)   #调用父类的FA方法
#         self.location='SY'  
#         self.area='dadong' 
#         #方法二：super()函数.方法名
#         '''super().__init__()     #super函数会将子类继承所有父类的方法'''
#     def  FA(self):  
#         print(2)    
# c=C1()
# # c.FA()  #c作为对象传给self：P1.__init__(c)，c.location='SH'
# print(c.location,c.area)
# '''
# 由于在调用父类的init的时候，c得到了‘location和area都为SH和songjiang‘，
# 但是能看到20和21行又赋予了子类location和area为SY和dadong，所以子类到底用哪个属性
# 也是和顺序有关系的。如果20和21删掉，就会继承父类的SH和songjiang了
# '''
# print(c.__dict__)
