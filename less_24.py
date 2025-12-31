student={
    'name':'Raees',
    'age':25,
    'course':'Python'
}
print(student['name'])
print(student['age'])
print(student['course'])
#if key does not exist Keyerror 
#print(studen['marks'])
student['mark']=85
student['age']=23
student.pop('course')
del student['age']
for key in student:
    print(key)
for value in student.values():
    print(value)
for key,value in student.items():
    print(key,':',value)
if 'name'in student:
    print('Name exist')
marks={
    'math':80,
    'science':75,
    'english':90,
}
total=0
for score in marks.values():
    total+=score 
print('total',total)
