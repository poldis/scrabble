x=input('Write a word:')
x=x.lower()
t=len(x)
n=0
k=0
while k!=t-1:
    if x[n]==x[t-(1+n)]:
        n=n+1
    else:
        print('No')
        exit(0)
    k=k+1
print('Yes')

