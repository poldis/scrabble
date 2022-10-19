x=input('Sag ein beliebtes Tier (mit Artikel):')
a=['die Kuh','der Schaf', 'der Hase', 'das Kaninchen','das Meereschwein', 'der Hund', 'die Katze', 'der Huhn', 'der Affe', 'die Schildkröte', 'die Ziege', 'das Pferd', 'der Schwein', 'die Pute', 'die Gans', 'der Wolf', 'der Elefant', 'die Giraffe','Maus']
b=['der Vogel', 'der Adler','der Falke','der Papagei','die Taube','der Rabe']
c=['die Qualle','das Seepferd','der Fisch','die Schildkröte','der Hai','der Wal','die Ente','der Schwan','der Krokodil','der Delfin']
if x=='die Schildkröte':
    print(x,'ist ein Tier an Land und kann auch sehr gut schwimmen')
    exit(0)
if x in a:
    print(x,'ist ein Tier an Land')
    exit(0)
if x in b:
    print(x,'hat Flügeln und kann fliegen')
    exit(0)
if x in c:
    print(x,'kann sehr gut schwimmen')
    exit(0)

print('Das Tier',x.split(' ')[1], 'kenne ich nicht')

