students={
    'name':'Raees',
    'marks':{
        'math':85,
        'science':90,
        'english':85
    }
}
print(students['marks']['math'])
students={
    'name':'Raees',
    'subject':['math','science','english']

}
print(students['subject'][0])
students=[
    {'name':'Raees','marks':80},
    {'name':'chishty','marks':90},
    {'name':'RC','marks':85},
]
for student in students:
    print(student['name'],student['marks'])
APIs={
    'status':'success',
    'users':[
        {'id':1,'name':"Raees"},
        {'id':2,'name':'Chishty'}
    ]
}
for api in APIs['users']:
    print(api['id'],api['name'])
students[0]['marks']=30
print(students)

jobs_role={
    'name':'TechCorp',
    'employees':[
        {'name':'Raees','role':'programmer'},
        {'name':'chishty','role':'developer'},
        
    ]
}
print(jobs_role[''],[''])