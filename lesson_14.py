#list example numbers=[1,2,3,4,5]
data=[1,'python',3.14,True]
print(data)
fruits=['apple','banana','mango']
print(fruits[0])
print(fruits[1])
print(fruits[2])

#nevigate indexing from end 
print(fruits[-1])
print(fruits[-2])

#changing list values(mutable)
fruits[1]='orange'
print(fruits)

#loop through a list(for loop)
fruits=['apple','banana','mango']
for fruit in fruits:
    print(fruit)

#adding items to a list 
#function used append() add at end 
fruits.append('grape')
print(fruits)

#removing items from a list 
#function used remove() by value 
fruits.remove('banana')
print(fruits)
#pop() remove by index 
fruits.pop(0)
print(fruits)

#function len()
print(len(fruits))

#check if item exists 
if 'apple'in fruit:
    print('apple is available')

