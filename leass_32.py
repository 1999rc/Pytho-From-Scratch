class Student:
    def __init__(self,name,age):
        self.name=name 
        self.age=age 
    def greet(self):
        print('hello',self.name)
s1=Student('Raees',25)
print(s1.name)
print(s1.age)
s1.greet()

class Bank_account:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount 
    def show_balance(self):
        print('balance:',self.balance)
acc=Bank_account(10000)
acc.deposit(500)
acc.show_balance()

class person_data:
    def __init__(self,name,age,city,work_type):
        self.name=name 
        self.age=age 
        self.city=city 
        self.work_type=work_type 
person=person_data('Raee',25,'badnwar','programming')
print(person.name)
print(person.age)
print(person.city)
print(person.work_type)
