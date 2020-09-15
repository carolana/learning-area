from random import shuffle

pessoa1 = input('Primeiro nome: ')
pessoa2 = input('Segundo nome: ')
pessoa3 = input('Terceiro nome: ')
pessoa4 = input('Quarto nome: ')
lista = [pessoa1, pessoa2, pessoa3, pessoa4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)