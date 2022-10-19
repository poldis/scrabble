import random
print('Welcome to hangman!')
letters=[]
list=['false','rainbow','attention','interaction','vocabulary','place','absolute','telephone','basketball','shoes','happy','bottle','qween','king','nice','help','football','purple','eleven','height','interview','meeting','writing','computer','life','beautiful','tired','snow','insect','polite','colorful','tiny','ball','detective','eggs','tomato','potato','angle','sport','maths','hard','medium','easy','india','germany']
word=random.choice(list)
l=10
t=0
n=0
z=0
k=['_' for i in range(len(word))]
print(k)
while '_' in k:
    x = input('Guess a letter:')
    if x in letters:
        print('You already had this letter')
        continue
    letters.append(x)
    if x in word:
        while n != len(word):
            if word[n] == x:
                z = z + 1
                k[n] = x
                n = n + 1
            else:
                n = n + 1
        n=0
        z=0
        print(k)
    else:
        l=l-1
        print("It isn't in the word. Now you've got",l,"more guesses")
    if l==0:
        print('You lose!:(')
        exit(0)
print('You won!:)')