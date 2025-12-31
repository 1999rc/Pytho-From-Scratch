class Students:
    def __init__(self,name):
        self.name=name 
s=Students('Raees')
print(s.name)
class Student1:
    def __init__(self,name):
        self._name=name 
s=Student1('Raees')
print(s._name)

class Student2:
    def __init__(self,name):
        self.__name=name 
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name=name 
s1=Student2('chishty')
print(s1.get_name())
s1.set_name('RC')
print(s1.get_name())

class Bank_acc:
    def __init__(self,balance):
        self.__balance=balance 
    def deposit(self,amount):
        if amount > 0:
           self.__balance+=balance
    def get_balance(self):
        return self.__balance

