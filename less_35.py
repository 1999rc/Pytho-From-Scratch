class Animal:
    def speak(self):
        print('Animal speaks!')
class Dogs(Animal):
    def speak(self):
        print('Dogs barks')
class Cat(Animal):

    def speak(self):
        print('Cat meows!')
animals=[Dogs(),Cat(),Animal()]
for a in animals:
    a.speak()
class Car:
    def move(self):
        print('Car moves!')
class Bike:
    def move(self):
        print('Bike moves!')
vehicles=[Car(),Bike()]
for v in vehicles:
    v.move()
def make_sound(obj):
    obj.speak()
make_sound(Dogs())
make_sound(Cat())

class Math:
    def add(self,a,b=0):
        return a+b 
m=Math()
print(m.add(5))
print(m.add(5,3))

class Payment:
    def pay(self):
        print('Processing payment...')
class UPI(Payment):
    def pay(self):
        print('Paid via UPI!')
class Card(Payment):
    def pay(self):
        print('Paid via Card!')
payments=[UPI(),Card()]
for p in payments:
    p.pay()
