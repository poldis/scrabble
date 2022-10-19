import random
num1=random.randint(1,15)
num2=random.randint(1,6)
x=input('Schreib hier ein beliebiges Wort:')
z=0
n=0
list=['a','e','i','o','u','A','E','I','O','U']
lastVokal = False
while n<=len(x)-1:
    if x[n] in list:
        if not lastVokal:
            z=z+1
        n=n+1
        lastVokal=True
    else:
        n=n+1
        lastVokal=False
print(x,'hat',len(x),'Buchstaben und',z,'Silben.')