import random
import math
list=['all numbers are same','the first and the last numbers are same','there are no numbers same',"there aren't same numbers","it's odd","it's even"]
list_2=[]
list_3=['1','3','5','7','9']
n=random.randint(2,10)
if n/2==n//2:
    list.remove("it's odd")
k=random.randint(3,6)
a=random.choice(list)
b=random.randint(50,100)
y=input('Do you want an easy or a hard level.')
if y=='hard':
    print('The number has got', k, 'digits, is divisible by', n, 'and', b, 'and', a, '.')
    x = input()
    t = True
    if len(x) == k:
        if int(x) / n == int(x) // n and int(x) / b == int(x) // b:
            if a == 'all numbers are same':
                for i in x:
                    if i != x[0]:
                        print("Wrong! The numbers aren't same!")
                        t = False
                if t:
                    print('Correct')
            if a == 'the first and the last numbers are same':
                if x[0] == x[len(x) - 1]:
                    print('Correct')
                else:
                    print("Wrong! The first and the last numbers aren't same!")
            if a == 'there are no numbers same' or a == "there aren't same numbers":
                for i in x:
                    if i not in list_2:
                        list_2.append(i)
                    else:
                        print('Wrong! Some numbers are same!')
                        t = False
                if t:
                    print('Correct')
            if a == "it's odd":
                if x[len(x) - 1] in list_3:
                    print('Correct')
                else:
                    print('Wrong!', x, 'is an even number')
            if a == "it's even":
                if x[len(x) - 1] not in list_3:
                    print('Correct')
                else:
                    print('Wrong!', x, 'is an odd number')
        else:
            print("Wrong! It isn't divisible by", n, "!")
    else:
        print('Wrong! It has got', len(x), 'letters but it must have', k, 'letters !')
if y=='easy':
    print('The number has got', k, 'digits, is divisible by', n,'and', a, '.')
    x = input()
    t = True
    if len(x) == k:
        if int(x) / n == int(x) // n:
            if a == 'all numbers are same':
                for i in x:
                    if i != x[0]:
                        print("Wrong! The numbers aren't same!")
                        t = False
                if t:
                    print('Correct')
            if a == 'the first and the last numbers are same':
                if x[0] == x[len(x) - 1]:
                    print('Correct')
                else:
                    print("Wrong! The first and the last numbers aren't same!")
            if a == 'there are no numbers same' or a == "there aren't same numbers":
                for i in x:
                    if i not in list_2:
                        list_2.append(i)
                    else:
                        print('Wrong! Some numbers are same!')
                        t = False
                if t:
                    print('Correct')
            if a == "it's odd":
                if x[len(x) - 1] in list_3:
                    print('Correct')
                else:
                    print('Wrong!', x, 'is an even number')
            if a == "it's even":
                if x[len(x) - 1] not in list_3:
                    print('Correct')
                else:
                    print('Wrong!', x, 'is an odd number')
        else:
            print("Wrong! It isn't divisible by", n, "!")
    else:
        print('Wrong! It has got', len(x), 'letters but it must have', k, 'letters !')
