def print_numbers():
    for i in range(1,6):
        print(i)
print_numbers()

def print_numbers(n):
    for i in range(1,n+1):
        print(i)
print_numbers(3)
print_numbers(7)

def sum_numbers(n):
    total=0 
    for i in range(1,n+1):
        total+=i
    return total
print(sum_numbers(5))

def check_password():
    correct_password="python123"
    for attempt in range(3):
        user_input=input('enter password')
        if user_input==correct_password:
            print('Login succesful!')
            return 
        else:
            print('wrong password!')
    print('account lcoked')
check_password()

def count_even_odd(numbers):
    even=0
    odd=0
    for num in numbers:
        if num %2==0:
            even+=1
        else:
            odd+=1
    return even,odd 
result=count_even_odd([1,2,3,4,5])
print(result)

def find_numbers(nums,target):
    for num in nums:
        if num==target:
            return 'found!'
    return 'not found!'
print(find_numbers([1,3,5,7],5))

def table(n):
    for i in range(1,11):
        print(n,'x',i,'=',n*i)
table(5)
def contains(lst,value):
    for item in lst:
        if item ==value:
            return True 
    return False 
print(contains([10,20,30,],2))


