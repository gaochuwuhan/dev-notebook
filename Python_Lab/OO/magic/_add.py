class In(int):
    def __add__(self,other):  
        return self + other

a=In('7')
b=In('2')
print(a+b)