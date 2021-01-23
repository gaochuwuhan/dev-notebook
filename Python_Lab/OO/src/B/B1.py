class B1:
  name='bai'
  def fun1(self,x,y):
    self.x=x
    self.y=y
    
class B11(B1):
  pass
def result(): 
  bb=B11()
  bb.fun1(1,2)
  #print(B1.__dict__)
  print(bb.x)

# del B1  #删除父类
# print(bb.x) #查看是否还有对象的x属性（注意：如果是执行这个python文件，则没有；如果是在交互下，还是有的，因为还在内存中）
# print(B1.__dict__)   #查看是否还有父类的内置属性（没了）
  
  