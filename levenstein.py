x=input('Say a word:')
y=input('Say another word:')
x=x.lower()
y=y.lower()
letters_x=list(x)
letters_y=list(y)
z=0
n=0
while z!=min(len(x),len(y)):
    if x[z]==y[z]:
        z=z+1
    else:
        n=n+1
        z=z+1
if len(x)==len(y):
    print(n)
else:
    for i in (set(x)&set(y)):
        letters_x.remove(i)
        letters_y.remove(i)
    print(max(len(letters_x),len(letters_y)))


