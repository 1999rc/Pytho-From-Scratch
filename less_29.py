file=open('data.txt','r')
content=file.read()
print(content)
file.close()

file=open('data.txt','r')

for line in file:
    print(line.strip())
file.close()

file=open('data.txt','w')
file.write('helloe world\n')
file.write('file handling lesson')
file.close()

file=ope('data.txt','a')
file.write('\nNew line added')
flie.close()

with open('data.txt','r')as file:
    content=file.read()
    print(content)
with open('data.txt','w')as file:
    file.write('program started')
with open('data.txt')as file:
    lines=f.readlines()
print(lines)
with open('data.txt','w')as file:
    f.write('math;80\n')
    f.write('science;90\n')
