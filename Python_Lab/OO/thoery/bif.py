class A:
  pass
class B(A):
  pass
class C:
  pass
b1=B()
print(isinstance(b1,B))
print(isinstance(b1,A)) #由于A是B的父类，所以返回True
print(isinstance(b1,(A,B,C)))  #ABC在一个元组中，至少一个为b1的类，就返回True
print(isinstance(b1,C))  #C不是b1的类

