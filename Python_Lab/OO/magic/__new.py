class CapStr(str):  #定义一个将字符串被改写为大写的类（这里str也是一个类）
  def __new__(cls, string): #cls是这个类,定义一个string参数
    string = string.upper()  #这里将我们的string参数重写，改为大写
    return str.__new__(cls,string) #将CapStr的new方法重新return，返回str基类的new方法，
    #此时已经重新将string参数改为大写，再套回旧的new方法就会改写这个类的new方法
print(CapStr("hello,bai"))