from abc import ABC,abstractmethod 
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass 
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14 *self.radius*self.radius 
c=Circle(5)
print(c.area())

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass 
class UPI(Payment):
    def pay(self,amount):
        print('Paid!',amount,'via UPI')
class Card(Payment):
    def pay(self,amount):
        print('Paid!',amount,'via Card')

 
