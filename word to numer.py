file=open('word to number.txt')
x = file.readline()
[word, number]=x.split(' ')
y=input('Say a number in letters:')
j=y.split('hundred')
if 'd' in y:
    if 'y' not in y:
        while word != j[0]:
            x = file.readline()
            [word, number] = x.split(' ')
        z = number
        while word != j[1]:
            x = file.readline()
            [word, number] = x.split(' ')
        q = number
        print(z + '0' + q)
    else:
        t=j[1].split('ty')
        while word != t[0]:
            x = file.readline()
            [word, number] = x.split(' ')
        z = number
        while word != j[1]:
            x = file.readline()
            [word, number] = x.split(' ')
        q = number
        while word != t[1]:
            x = file.readline()
            [word, number] = x.split(' ')
        c = number
        print(q+z+c)