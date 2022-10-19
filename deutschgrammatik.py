x=input('Schreibe hier einen Satz, welcher die 3.Person Singular enthält.')
n= x.split(' ')[0]
v=['mag','spielt','geht','schreibt','ist','macht','hat','isst','läuft','rennt','steht','lacht','wo','wann','wie','was','wodurch','wieso','warum','weshalb']
u=['wohnt','spielt','macht','hat','lachte','sagte']
if set(x.split(' ')) & set(v + u) == set():
    print('Leider kenne ich diesen Satz nicht:(')
    exit(0)
a=input('Schreibe hier den Verb im Invinitiv des vorherigen Satzes.')
if n in v:
    y='ein Fragezeichen.'
else:
    y='ein Punkt.'
if n in u:
    z='regelmäßiges'
else:
    z='unregeläßiges'
print("Das Satzzeichen des Satzes ist",y,"'",a,"' ist ein",z,"Verb")



