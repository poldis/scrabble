# 1. Wir öffnen ein Wörterbuch
import itertools
import collections
import random
from itertools import repeat
def read_dictionary():
    alle_woerter = set()
    my_file = open("deutsches_Woerterbuch.txt", "r")
    # Benutze READLINE um ein Wort nachdem anderen zulesen, mit Hilfe von LOWER,
    # Und addiere zu SET
    myline = my_file.readline()
    while myline:
        alle_woerter.add(myline.strip().lower())
        myline = my_file.readline()
    my_file.close()
    print(alle_woerter)
    my_file.close()
    return alle_woerter

def get_valid_words(alle_woerter, gestell):
    # Mit Blanko alle Wörter bilden
    possible=[]
    for suche in range(0,7):
        if gestell[suche]=='*':
            starlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            for i in starlist:
                gestell[suche]=i

                for r in range(1, 8):
                    alle_kombinationen = list(itertools.permutations(gestell, r))
                    for kombi in alle_kombinationen:
                        kombi = ''.join(kombi)
                        if kombi in alle_woerter:
                            possible.append(kombi)
        # Ohne Blanko alle Wörter bilden
        else:
            for r in range(1, 8):
                alle_kombinationen = list(itertools.permutations(gestell, r))
                for kombi in alle_kombinationen:
                    kombi = ''.join(kombi)
                    if kombi in alle_woerter:
                        possible.append(kombi)
    return possible

def punkte_berechnen(possible,d):
    punktliste = {}
    for wort in possible:
        points = 0
        for buchstabe in wort:
            points += d[buchstabe]
        punktliste[wort] = points
    #sorted_punktliste = sorted(punktliste.items(), key=lambda x: x[1])
    sorted_punktliste = collections.OrderedDict(punktliste.items())
    return sorted_punktliste

def ergebnisse_drucken(gestell,possible,d):
    sorted_punktliste = punkte_berechnen(possible,d)
    if possible!=[]:
        for (key, value) in sorted_punktliste.items():
            print(key, "->", value)
    else:
        print('Es gibt kein Wort mit den Buchstaben',gestell[0]+',',gestell[1]+',',gestell[2]+',',gestell[3]+',',gestell[4]+',',gestell[5],'und',gestell[6]+'.')

def board_in_list():
    board=list()
    my_board = open("board.txt", 'r')
    line = my_board.readline()
    while line:
        board.append(line.strip().split(' '))
        line = my_board.readline()
    print(board)
    my_board.close()
    return board

def board_punkte(possible, d, board):
    possible_2=[]
    diraction=input('diraction:')
    row=int(input('row:'))
    spalte=int(input('spalte:'))
    if diraction=='right':
        for wort in possible:
            if len(wort) <= 16 - int(spalte):
                possible_2.append(wort)
        for wort in possible_2:
            most_points = 0
            total_times = 1
            s = spalte
            for buchstabe in wort:
                print("came with", buchstabe, d[buchstabe] , row, s, board[row-1][s-1])
                if board[row-1][s-1] == '00':
                    most_points = most_points + d[buchstabe]
                if board[row-1][s-1] == 'DL':
                    most_points=most_points + (d[buchstabe]*2)
                if board[row-1][s-1] == 'TL':
                    most_points=most_points + (d[buchstabe]*3)
                if board[row-1][s-1] == 'DW':
                    most_points=most_points+d[buchstabe]
                    total_times = 2
                if board[row-1][s-1] == 'TW':
                    most_points = most_points + d[buchstabe]
                    total_times = 3
                s+=1
            most_points *= total_times
            print(wort+'-->',most_points)
    if diraction == 'down':
        for wort in possible:
            if len(wort) <= 16 - row:
                possible_2.append(wort)
        for wort in possible_2:
            most_points = 0
            total_times = 1
            r = row
            for buchstabe in wort:
                print("came with", buchstabe, r, spalte, board[r-1][spalte-1])
                if board[r-1][spalte-1] == '00':
                    most_points = most_points + d[buchstabe]
                if board[r-1][spalte-1] == 'DL':
                    most_points=most_points + (d[buchstabe]*2)
                if board[r-1][spalte-1] == 'TL':
                    most_points=most_points + (d[buchstabe]*3)
                if board[r-1][spalte-1] == 'DW':
                    most_points=most_points+d[buchstabe]
                    total_times = 2
                if board[r-1][spalte-1] == 'TW':
                    most_points = most_points + d[buchstabe]
                    total_times = 3
                r+=1
            most_points *= total_times
            print(wort+'-->',most_points)
    #print(possible_2)

def get_seven_letters():
    bag=list()
    bag.extend(repeat('a', 5))
    bag.extend(repeat('b', 2))
    bag.extend(repeat('c', 2))
    bag.extend(repeat('d', 4))
    bag.extend(repeat('e', 15))
    bag.extend(repeat('f', 2))
    bag.extend(repeat('g', 3))
    bag.extend(repeat('h', 4))
    bag.extend(repeat('i', 6))
    bag.extend(repeat('j', 1))
    bag.extend(repeat('k', 2))
    bag.extend(repeat('l', 3))
    bag.extend(repeat('m', 4))
    bag.extend(repeat('n', 9))
    bag.extend(repeat('o', 3))
    bag.extend(repeat('p', 1))
    bag.extend(repeat('q', 1))
    bag.extend(repeat('r', 6))
    bag.extend(repeat('s', 7))
    bag.extend(repeat('t', 6))
    bag.extend(repeat('u', 6))
    bag.extend(repeat('v', 1))
    bag.extend(repeat('w', 1))
    bag.extend(repeat('x', 1))
    bag.extend(repeat('y', 1))
    bag.extend(repeat('z', 1))
    bag.extend(repeat('ä', 1))
    bag.extend(repeat('ö', 1))
    bag.extend(repeat('ü', 1))
    bag.extend(repeat('*', 2))
    f=random.sample(bag, 7)
    print('Hier sind deine sieben Buchstaben:',f)
    gestell = [f[0], f[1], f[2], f[3], f[4], f[5], f[6]]
    return gestell

d = {'a': 1, 'ä': 6, 'b': 3, 'c': 4, 'd': 1, 'e': 1, 'f': 4, 'g': 2, 'h': 2, 'i': 1, 'j': 6, 'k': 4, 'l': 2, 'm': 3,
         'n': 1, 'o': 2, 'p': 4, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 6, 'w': 3, 'x': 8, 'y': 10, 'z': 3}
alle_woerter = read_dictionary()
gestell = get_seven_letters()
possible = get_valid_words(alle_woerter, gestell)
ergebnisse_drucken(gestell,possible,d)
board = board_in_list()
board_punkte(possible,d, board)