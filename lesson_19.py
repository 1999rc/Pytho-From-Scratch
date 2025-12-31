def print_list(items):
    for item in items:
        print(item)
print_list([10,20,30,40])
def sum_list(numbers):
    total=0
    for num in numbers:
        total+=num 
    return total 
print(sum_list([1,2,3,4,5]))
def find_maximum(values):
    max_value=values[0]
    for num in values:
        if num > max_value:
            max_value=num 
    return max_value
print(find_maximum([3,7,2,9,4]))
def get_even(val):
    evens=[]
    for num in val:
        if num%2==0:
            evens.append(num)
    return evens 
print(get_even([1,2,3,4,5,6]))
def count_greater(number,limit):
    count =0 
    for num in number:
        if num > limit :
            count+=1
    return count 
print(count_greater([10,20,30,40,],25))

def search(items,target):
    for item in items :
        if item ==target:
            return 'found!'
    return 'not found'
print(search(['apple','banana','mango','banana'],'cherry'))
def average(Numbers):
    return sum(Numbers)/(len(Numbers))
print(average([10,20,30]))
def remove_negative(Nums):
    result=[]
    for num in Nums:
        if num > 0:
            result.append(num)
    return result 
print(remove_negative([-1,2,-3,4]))
def count_long_numbers(words):
    count =0 
    for word in words:
        if len(word)>3:
            count+=1 
    return count 
print(count_long_numbers(['log','hi','no','love','nice']))



