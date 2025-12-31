def square(x):
    return x*x 
square=lambda x:x*x 
print(square(5))
add=lambda a,b:a+b 
print(add(3,4))
nums=[1,2,3,4]
square=list(map(lambda x:x *x,nums))
print(square)
nums=[1,2,3,4,5,6]
evens=list(filter(lambda x:x %2==0,nums))
print(evens)
nums=[1,2,3,4,5,6]
[x for x in nums if x %2==0 ]
def double(x):
    return x*2 
print(list(map(double,nums)))
def is_even(x):
    return x%2 ==0

print(list(filter(is_even,nums)))
price=[100,200,300,400]
gst_price=list(map(lambda p:p+p*0.18,price))
print(gst_price)
