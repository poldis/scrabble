y=2
isPrime=True
x=int(input('Say a random number'))
while True:
    if y==x:
        break
    if x/y==x//y:
     print("It's divisible by",y)
     isPrime=False
    y=y+1
if isPrime:
    print("It's prime")
else:
    print("It's not prime, I wrote the divisor(s) above!")
