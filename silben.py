import random
num1=random.randint(1,15)
num2=random.randint(1,6)
x=input('Schreib hier ein beliebiges Wort:')
z=0
n=0
y=int(input('Wie viele Zwielaute hat dieses Wort?'))
list=['a','e','i','o','u','A','E','I','O','U']
while n<=len(x)-1:
    if x[n] in list:
        z=z+1
        n=n+1
    else:
        n=n+1
if z-y<=0:
    print('Dieses Wort kenne ich nicht')
    exit(0)
if z-y==1:
    print(x,'hat',len(x),'Buchstaben und eine Silbe.')
else:
    print(x,'hat',len(x),'Buchstaben und',z-y,'Silben.')