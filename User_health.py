"""
Program Name ; User Health & Statistics Analizer 
Lesson :x4
Purpose :Input validation,math,statistics & 
HTML reporting 
Autor   :Raees (Learning Python)
"""

import math 
import statistics 

#=======INPUT + VALIDATION==========

name=input('Enter your name:').strip()

while True:
    try:
        age=int(input('Enter your age:'))
        if age <=0:
            raise ValueError
        break 
    except ValueError:
        print('Age must be a positive number.')
while True:
    try:
        height_cm=float(input('Enter height in cm.'))
        if height_cm <=0:
            raise ValueError
        break 
    except ValueError:
        print('Height bust be positive number.')
while True:
    try:
        weight_kg=float(input('Enter weight in kg.'))
        if weight_kg <=0:
            raise ValueError
        break 
    except ValueError:
        print('Weight must be a positive number.')
active_input=input('Are active? (yes/y/no/n):').lower()
is_active=active_input in ('yes','y')

#======MATH & STATISTICS================

height_m=height_cm/100
bmi=weight_kg/math.pow(height_m,2)
bmi=round(bmi,2)

#Fake dataset for teaching statistics 
weekly_steps=[4500,7000,8200,6100,9000,10000,7500]

avg_steps=int(statistics.mean(weekly_steps))
max_steps=max(weekly_steps)
min_steps=min(weekly_steps)

#==========BMI INTERNATIONAL===================

if bmi <18.5:
    bmi_status='Underweight'
elif bmi <25:
    bmi_status='Normal'
elif bmi <30:
    bmi_status='Overweight'
else:
    bmi_status='Obese'

html_content=f"""
<!DOCTYPE html>
<html>
<head>
 <title>User Health Report</title>
 <style>
 body {{
    font-family:Arial;
    background:#f4f6f8;
    padding:20px;
 }}
 .card {{
    background:white;
    padding:20px;
    border-radius:10px;
    max-width:500px;
    margin:auto;
    box-shadow:0 0 10xp rgba(0,0,0,0,1);
 }}
  h2 {{color:#2c3e50;}}
    .good {{color:gree;}}
    .bad{{color:red;}}
 </style>
</head>
<body>
 <div class="card">
   <h2>User Health Report</h2>
   <p><b>Name:</b>{name}</p>
   <p><b>Age:</b>{age}</p>
   <p><b>Active:</b>{is_active}</p>

   <h3>Body Metrics</h3>
   <p>Height:{height_cm}cm</p>
   <p>Weight:{weight_kg}kg</p>
   <p><b>BMI:</b>{bmi}({bmi_status})</p>

   <h3>Weekly Activity(Steps)</h3>
   <p>Average:{avg_steps}</p>
   <p>Max:{max_steps}</p>
   <p>Min:{min_steps}</p>
 </div>
 </bdoy>
 </html>
 """

with open('user_report.html','w')as file:
    file.write(html_content)
print('\n Report generated: user_report.html (Open in browser)')

'''
Enter your name:Raees chishty
Enter your age:25
Enter height in cm.6.3
Enter weight in kg.59.800
Are active? (yes/y/no/n):y

 Report generated: user_report.html (Open in browser)
 '''
 
  