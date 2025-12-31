try:
    x=int(input('enter a number'))
    print(10/x)
except:
    print('something went wrong!')
try:
    x=int(input('enter a number:'))
    print(10/x)
except ValueError:
    print('please enter a valid number!')
except ZeroDivisionError:
    print('cannot divide by zero!')

try:
    x=int(input('enter a number:'))
except ValueError:
    print('invalid input!')
else:
    print('you entered:',x)
try:
    file=open('data.txt','r')
    print(file.read())
except FileNotFoundError:
    print('file not found!')
finally:
    print('Done')
try:
    with open('info.txt')as fp:
        print(fp.read())
except FileNotFoundError:
    print('file does not exist!')
def withdraw(amount):
    if amount <=0:
        raise ValueError('Amount must be positve!')
    print('Withdraw!',amount)
