numbers=[10,20,30,40]
names=['raees','chishty','rc']
print(numbers[0],names[0])
print(numbers[1],names[1])
print(numbers[2],names[2])
numbers[1]=99
names[2]=22
print(numbers,names)
#print(len(numbers))
print(len(names))
for num in numbers:
    for n in names:
        print(num)
    
        print(n)
fruits=['apple','banana','mango']
print(fruits[0])
fruits[1]='orange'
for fruit in fruits:
    print(fruit)
l=[1,2,3]
l.append(4)
print(l)
l1=[1,2,3]
l1.insert(1,99)
print(l1)
l1.remove(2)
print(l1)
l2=[10,20,30]
x=l2.pop(1)
print(x)
print(l2)
#if not index then l2.pop()remove last item
l3=[1,2,3,4]
l3.clear()
print(l3)
l4=[10,20,30,40]
print(l4.index(20))
l4=[1,2,3,2]
print(l4.count(2))
l5=[3,1,4,2]
l5.sort()
print(l5)
l5.sort(reverse=True)
print(l5)
l6=[1,2,3]
l6.reverse()
print(l6)

marks=[]

marks.append(80)
marks.append(90)
marks.append(70)
marks.sort()
print("Highest",marks[-1])
print("All marks",marks)
