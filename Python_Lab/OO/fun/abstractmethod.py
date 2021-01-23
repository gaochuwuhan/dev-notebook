
from abc import ABC, abstractmethod
class P(ABC):
    @abstractmethod
    def f1(self):
        print('x')
    def f3(self):
        print('z')
        self.f1()
    
class C(P):
    def f1(x):
        print('xx')
    def f2(y):
        print('y')
    def f3(z):
        print('zz')
c=C()
c.f1()
    
