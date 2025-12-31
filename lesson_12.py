count =1 
while count <=5 :
    print(count)
    count=count +1 

passwords=""
while passwords.strip() != "python":
    passwords=input("enter your passwords here!")
    print("DEBUG",passwords)
print("Access granted")

while True :
    number=int(input("enter a number:"))
    if number ==0:
        break 
    print("you enterd",number)

count =0
while count <5:
    count +=1 
    if count ==3:
        continue 
    print(count)
x=3 
while x > 0:
    print(x)
    x-=1 
correct_passwords="python"
attempts=0
max_attempts=3
while attempts < max_attempts:
    passwords=input('enter your passwords here!')
    if passwords ==correct_passwords:
        print("access granted")
        break 
    else :
        attempts +=1 
        print("wrong passwords")
if attempts==max_attempts:
    print("Access denied:too many attempts")


