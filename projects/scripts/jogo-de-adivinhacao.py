#numero = int(input('Digite um número inteiro entre 0 e 5: '))
#if numero == 4:
    #print('Parabéns! Você conseguiu!!!')
#else:
    #print('Você errou! Tente novamente...')


from random import randint
computador = range(0, 5) #Faz o computador pensar
print('+' * 30)
print('Vou pensar em um número entre 0 e 5...')
print('+' * 30)
jogador = int(input('Em que número eu pensei: '))
if jogador == computador:
    print('Parabéns, você conseguiu me vencer!!!!')
else:
    print('Ihhhh... Que pena! Você perdeu...')