"""
Program Name:User Profile Builder 
Lesson:x2 Variables & Data Types 
Author:Raees (Learning Python)
Purpose:Demonstrate real-world usage of basic
data types
"""
#User details (input Layer)
name='Raees chishty' #string
age=25               #intger
height_cm=172.5      #float 
is_active_user=True  #boolean

#Business local layer 
birth_year =2025  -age 
height_m = height_cm/100

#Output layer (professional formatted output)
print('=======USER PROFILE REPORT=========')
print('Name      :',name)
print('Age       :',age)
print('Birth year:',birth_year)
print('Height (cm):',height_cm)
print('Height (meter):',height_m)
print('Active User :',is_active_user)

'''
=======USER PROFILE REPORT=========
Name      : Raees chishty
Age       : 25
Birth year: 2000
Height (cm): 172.5
Height (meter): 1.725
Active User : True
'''
