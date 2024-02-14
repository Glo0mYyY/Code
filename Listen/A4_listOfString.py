woerter = ['Hallo','Hello','holla','ciao','salut','hola','hej','hei','hej']
referenzWort = 'Halo'

for wort in woerter:
    if (wort[0]) == referenzWort[0] and (wort[-1]) == referenzWort[-1] and len(wort) >= 2:
        print(wort)
        