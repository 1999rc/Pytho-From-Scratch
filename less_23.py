nums={1,2,2,3,4}
print(nums)
#no indexing in sets
"""
Example
print(nums[0])
And this will raise an Error:
"""
nums={1,2}
nums.add(3)
print(nums)
"""
don't delete from remove 
do this!
print(nums.dicard(3)) 
not this!
print(nums.remove(3))
this will raise an Error:
"""
fruits={'apple','banana','mango'}
for fruit in fruits:
    print(fruit)
a={1,2,3}
b={3,4,5}
print(a|b)
print(a & b)
print(a -b)
nums={1,2,2,3,3}
unique_nums=set(nums)
x=unique_nums
print(x)
languageg={'Python','java','c'}
if "Python"in languageg:
    print('skill found!')
else:
    print('no')
skills1={'python','git','linux'}
skills2={'python','docker'}
print(skills1 & skills2)



