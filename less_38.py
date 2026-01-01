person={
    'id':101,
    'name':'Raees',
    'course':'Python',
    'marks':{
        'math':85,
        'science':90,
        'english':88
    }
}
print(person['name'])
print(person['marks']['science'])

persons=[
    {'name':'Raees','age':25},
    {'name':'chishty','age':23},
    {'name':'RC','age':13}
]
print(persons[1]['name'])
for x in persons:
    print(x['name'],x['age'])
for subject,marks in person['marks'].items():
    print(subject,':',marks)

data={
    'status':'success',
    'count':2,
    'users':[
        {
            'id':1,
            'name':'Raees',
            'skills':['Python','linux','git']
        },
        {
            'id':2,
            'name':'chishty',
            'skills':['LINUX','Docker']
        }
    ]
}
print(data['users'][0]['skills'][0])

company={
    'name':'TechCorp',
    'employees':[
        {
            'name':'Raees',
            'role':'developer',
            'skills':['Python','GIT']
        },
        {
            'name':'chishty',
            'role':'Devops',
            'skills':['Linux','Docker']
        }
    ]
}
for emp in company['employees']:
    print(emp['name'])
    print('skills')
    for skill in emp['skills']:
        print('-',skill)
    print()
