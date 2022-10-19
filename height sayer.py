f = open('viyona_aalu.txt')
num=0
x = f.readline()
while x:
    [name, height] = x.split(' ')
    print(name, 'is ', int(height)-4, 'cms tall.')
    x = f.readline()

