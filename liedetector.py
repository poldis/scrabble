print ('I will tell you, whether you lie or not. At least in one of this two questions you must give the right answer.')
x = int(input('How old are you? Answer:'))
y = input("What's your name? Answer:")
if x!=10 and x!=39 and x!=40:
    print ('You are lying! :(')
    exit(0)
namesAV=['Aarav','Aarav Singh','Aalu','Aalu Singh','Viyona', 'Viyona Singh','Vivi','Vivi Singh', 'VV', 'VV Singh']
namesP=['Papa','Papa Singh','Vasu','Vasu Singh']
namesM=['Mama','Mama Singh','Anmol','Anmol Singh']
if x==10 and y not in namesAV:
    print ('You are lying! :(')
    exit(0)
if x==40 and y not in namesP:
    print ('You are lying! :(')
    exit(0)
if x==39 and y not in namesM:
    print ('You are lying! :(')
    exit(0)
print ("You aren't lying :)")