import time
import random
print('Welcome to most_letter_game!')
n=0

start=time.time()
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
points=0
def most_letter(m):
    d={}
    for i in m:
        d[i] = d.get(i, 0) + 1
        #if i in d:
        #    d[i]+=1
        #else:
        #    d[i]=1
    return (max(d, key=d.get))
while True:
    r1 = random.choice(letters)
    r2 = random.choice(letters)
    r3 = random.choice(letters)
    r4 = random.choice(letters)
    r5 = random.choice(letters)
    word_letters = [r1, r2, r3, r4, r5]
    word = random.choice(word_letters) + random.choice(word_letters) + random.choice(word_letters) + random.choice(
        word_letters) + random.choice(word_letters) + random.choice(word_letters) + random.choice(
        word_letters) + random.choice(word_letters) + random.choice(word_letters) + random.choice(
        word_letters) + random.choice(word_letters)
    print(word)
    x=input("What's the most letter?")
    correct_answer = most_letter(word)
    if x==correct_answer:
        print('Correct')
        points+=1
    else:
        print('Wrong, the right answer is',correct_answer)
    if time.time()-start>60:
        break
print('Time up!')
print("You've got",points,"points!")

