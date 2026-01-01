"""
Program Name:Inter-active-user-profile-builder
Lesson:x3 - User Input & Type Casting 
Author:Raees (Learning Python) 
Purpose:Collect user input and generate a profile 
report 
"""

#=====INPUT LAYER=====
name=input('Please enter your full name::')

age=int(input('Please enter your age here!'))

height_cm=float(input('Please enter your height in cm::'))

active_input=input('Are you an active user? (yes/no):'.lower())

#======LOGIC LAYER======
current_year=2025
birth_year=current_year-age 
height_m=height_cm/100

if active_input=='yes':
    is_active_user=True 
else:
    is_active_user=False 

#=======OUTPUT LAYER=====
print('\n=====USER PROFILE REPORT======')
print('Name      :',name)
print('Age       :',age)
print('Birth Year:',birth_year)
print('Height (cm):',height_cm)
print('Height (meter):',height_m)
print('Active User   :',is_active_user)
print('==================================')

'''
Please enter your age here!25
Please enter your height in cm:6.3
are you an active user? (yes/no):y

=====USER PROFILE REPORT======
Name      :  Raees chishty
Age       : 25
Birth Year: 2000
Height (cm): 6.3
Height (meter): 0.063
Active User   : False this must be inside "yes"
==================================
'''