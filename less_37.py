person_data={
    'name':'Raees',
    'age':22,
    'course':'Python',
    'email':'raees@gamilc.com'
}
print(person_data)
print(person_data['name'])
print(person_data['age'])
print(person_data['email'])
x=person_data
x['age']=23
print(x['age'])
print(x.pop('course'))
del x['email']
for key in x:
    print(key)
for value in x:
    print(value)
print(x)
for key,value in x.items():
    print(key,':',value)
print(x.keys())
print(x.values())
print(x.items())

person={
    'name':'Raees',
    'city':'badnawar',
    'skills':['Python','git','linux']
}
person['experience']=1
for key,value in person.items():
    print(key,':',value)

