
# This program generates password with characters, upper and lower case letter, digits and specjal sings
# Author Przemysła Książek Vickul

import random

character = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'r', 's', 'ś', 't', 'u', 'w', 'y', 'z', 'ź', 'ż','q','v', 'x',
        'A', 'Ą', 'B', 'C', 'Ć', 'D', 'E', 'Ę', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Ł', 'M', 'N', 'Ń', 'O', 'Ó', 'P', 'R', 'S', 'Ś', 'T', 'U', 'W', 'Y', 'Z', 'Ź', 'Ż',
        '1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','(',')','+','-','=','{','}',':','|','?','<','>','/', '\\' '`', '_']

print('Witaj w generatorze haseł.')
print('Dobre hasło powinno zawierać co najmniej 10 zanków i zawierać duże i małe litery, cyfry oraz znaki specjalne')
howManyCharacters = int(input('Ile znaków ma mieć twoje hasło? Podaj liczbę: '))
#print(howManyCharacters)
yourPassword = ''
flag = True

while flag:

    if howManyCharacters >= 10:

          for char in range(1, howManyCharacters + 1):
              yourPassword += (character[random.randint(1, len(character)-1)])
              #print(yourPassword)
              flag = False

    else:
        print('Bezpieczne hasło musi zawierać conajmniej 10 znaków a Twoje hasło będzie miało {}'.format(howManyCharacters))
        howManyCharacters = int(input('Ile znaków ma mieć twoje hasło? Podaj liczbę: '))

print('To Twoje wygenerowane hasło: {}'.format(yourPassword))
print('\nZalecam zapisanie hasło bo nie będziesz w stanie go zapamiętać :)')
print('\nDziękuje za skorzystanie z mojego generatora haseł')