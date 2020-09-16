frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A primera letra A está na posição {}'.format(frase.find('A')))
print('A últina letra A está na posição {}'.format(frase.rfind('A')))