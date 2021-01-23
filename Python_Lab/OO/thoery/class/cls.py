class Bai:
    name=None
    age=None
    work=None
    def __init__(self,name,age,work):
        self.name=name
        self.age=age
        self.work=work
    def printName_Age(self):
        print("我叫"+self.name+","+"今年"+str(self.age)+"岁。")
    def printWork(self):
        print("工作是",self.work)
    def printTotal(self):
        print("类中方法调用其他方法")
        Bai.printName_Age(self)   #类名.方法名(self)
        Bai.printWork(self)
bai=Bai('xiaobai',18,'devops')
bai.printTotal()