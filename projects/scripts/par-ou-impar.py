numero = int(input('Digite um número e vou adivinhar se é par ou ímpar: '))
resto = (numero % 2) 

if resto == 0:
    print('O número {} é par'.format(numero))
else:
    print('O número {} é ímpar'.format(numero))
