def greet():
    print('hello,python!')
greet()
def greet(name):
    print('hello',name)
greet('Raees')
def add(a,b):
    return a+b 
result=add(3,5)
print(result)

def math_ops(a,b):
    return a+b,a-b 
sum_,diff=math_ops(10,5)
print(sum_,diff)

def greet(name='Guest'):
    print('hello',name)
greet()
greet('Raees')

def student(name,age):
    print(name,age)
student(age=22,name='Raees')
x=10
def test():
    x=5 
    print(x)
test()
print(x)

def total(*numbers):
    s=0 
    for n in numbers:
        s+=n 
    return s 
print(total(1,2,3,4))
def profile(**info):
    for k,v in info.items():
        print(k,v)
profile(name='Raees',skill='Python',level='beginner')
profile()
def calculate_percentage(total,obtained):
    return (obtained/total)*100
print(calculate_percentage(500,420))

