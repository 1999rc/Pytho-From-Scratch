numbers=[10,20,30,40,50]
print(numbers[1:4])

#slicing from start to end 
print(numbers[:3]) #from start 
print(numbers[2:]) #till end 

#nevidate slicing 
print(numbers[-3:])
#and the output [30,40,50]

#step in slicing 
print(numbers[::2])
#and the output is:[10,30,50]
"""
Another:Example
"""
names=["Mohommed","Raees","Chishty","RC","rc"]
print(names[::2])
#and the output is["Mohommed","Chishty","rc"]
#reverse a list (Classic Trick)
print(numbers[::-1])
#and the output is:[50,40,30,20,10]

#common list methods
numbers.append(60) #taken 1 argument 

numbers.insert(1,23) #taken two arguments 

numbers.extend([13,45,29]) #multiple arguments 

numbers.remove(13) #One argument 

numbers.pop(0)#that means [1]

numbers.clear()

#sorting list 
nums=[3,1,4,2]
nums.sort()
print(nums)
#and the output is:[1,2,3,4]
#reverse sort 
nums.sort(reverse=True)

nums=[1,2,2,4]
print(nums.count(2))
#and the output is:2 
print(nums.index(4))
#and the output is:3 

#copying a list 
a=[1,2,3]
b=a.copy()

x=[1,2,3,4,5]
y=x[1:4]
y.append(10)
print("the value of x:is",x)
print("the value of y:is",y)