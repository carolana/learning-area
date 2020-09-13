#isnumeric
#isalpha
#isalnum
#print(variavel.isalgo())
#isupper

algo = input('Digite algo: ')
print('O tipo deste dado é ', type(algo))
print('Só tem espaço? ', algo.isspace())
print('Só tem letras? ', algo.isalpha())
print('É alfanumérico? ', algo.isalnum())
print('É numérico? ', algo.isnumeric())
print('Está escrito apenas em letras minusculas? ', algo.islower())
print('E apenas maisuculas? ', algo.isupper())
