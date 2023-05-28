import itertools

string = input('String a se testar combinações possiveis: ')

resultado = itertools.permutations(string, len(string))

contador = 0

for i in resultado:
    print(''.join(i))
    contador+= 1

print('-' * 10)

print('Numero de combinações possiveis: ', contador)