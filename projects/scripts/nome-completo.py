nome = str(input('Digite seu nome completo: ')).split
print('Seu nome com todas as letras maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome)- nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))