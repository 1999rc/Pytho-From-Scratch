def say_hello():
    print("Hello")
say_hello()
say_hello()
say_hello()

def greet():
    print("welcome to python:")
greet()

def greet_user(name):
    print("hello",name)
greet_user("raees")
greet_user("python")

def add(a,b):
    print(a+b)
add(5,3)
add(10,20)

def add(a,b):
    return a+b
result=add(4,6)
print(result)

def check_password(password):
    if password=='adimin123':
       return 'Access granted'
    else:
        return 'Access denied'
print(check_password('admin123'))
print(check_password('hello'))

def my_name():
    print('your name')
my_name()

def multiply(a,b):
    return a*b 
print(multiply(3,4))

def even_odd(number):
    if number % 2==0:
        return('even')
    else :
        return 'odd'
print(even_odd(7))


