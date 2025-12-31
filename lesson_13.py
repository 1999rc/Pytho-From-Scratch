for i in range(5):
    print(i)

for i in range(1,6):
    print(i)
for i in range(1,10,2):
    print(i)
name="python"
for letter in name :
    print(letter)
correct_passwords='python'
for attempts in range(1,4):
    passwords=input('attempt {attempt}')
    if passwords ==correct_passwords:
        print("access granted")
        break 
else:
    print("access denied:too many attempts")
