import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
#print('A raiz quadrada do número {} é {:.2f}'.format(num, raiz))
print('A raiz quadrada do número {} é {}'.format(num, math.ceil(raiz))) #usando o método ceil para arredondar para cima o resultado da raiz quadrada do número
