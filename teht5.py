
käyt1 = input('Anna käyttäjänimi: ')
sals1 = input('Anna salasana: ')
while (käyt1!=str('Python') and sals1!=str('Rules')):
    if käyt1!=str('Pyhton') or sals1!=str('Rules'):
        print('Pääsy evätty')
    käyt1 = input('Anna käyttäjänimi: ')
    sals1 = input('Anna salasana: ')

print('Tervetuloa')