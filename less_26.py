squars=[]
for i in range(1,6):
    squars.append(i * i)
squars=[i * i for i in range(1,6)]

nums=[1,2,3,4]
double=[n* 2 for n in nums]
print(double)
nums=[1,2,3,4,5,6]
evens=[n for n in nums if n %2 ==0]
print(evens)
names=['1','2','3']
nums=[int(n)for n in names]
print(nums)
marks={'math':80,'science':90}
bonus={k:v+5 for k,v in marks.items()}
print(bonus)
passed={k:v for k,v in marks.items()if v>=85}
nums=[1,2,2,3,4]
unique=[n for n in nums]
print(unique)
