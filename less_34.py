class Animal:
    def speak(self):
        print("Animal makes a sound!")
class Dog(Animal):
    pass 
d=Dog()
d.speak()
class Dog(Animal):
    def bark(self):
        print('Dog barks')
d=Dog()
d.speak()
d.bark()
class Animal:
    def speak(self):
        print('Animal sound!')
class Cat(Animal):
    def speak(self):
        print('Meow!')
c=Cat()
c.speak()
class Animal:
    def __init__(self,name):
        self.name=name 
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed 
d=Dog('Tommy','Labbrador')
print(d.name,d.breed)
class A:
    def show(self):
        print('A')
class B:
    def display(self):
        print('B')
class C(A,B):
    pass 
c=C()
c.show()
c.display()
class Employee:
    def __init__(self,name,salary):
        self.name=name 
        self.salary=salary 
class Manage(Employee):
    def bonus(self):
        return self.salary*0.2
m=Manage('Raees',50)
print(m.bonus())