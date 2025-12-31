colors=('red','gree','blue')
print(colors[0]) #and the output is:red 
print(colors[-1]) #and the output is:blue 
#immutable means
"""
colors[1]='yellow' Error:
"""
print(len(colors)) #and the output is:3 
for color in colors:
    print(color)
x=(5)
print(type(x)) #and the output is:<class 'int'> X 
x=(5,)
print(type(x)) #and the output is:<class 'tuple'> 
person=('Raees',25,'india')
name,age,country=person
print(name)
print(age)
print(country)
student=("Raees",22,"Python")
for item in student:
    print(item)
    

