import random

num = int(random.randint(1, 10))
arvaus = int(input('Arvaa numero: '))
while arvaus != num:
    if arvaus > num:
        print('Liiän suuri arvaus')
    if arvaus < num:
        print('Liiän pieni arvaus')
    arvaus = int(input('Arvaa uudestaan: '))
print('Oikein')