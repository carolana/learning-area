carteira = float(input('Quanto dinheiro você tem na carteira? R$ '))
print('Você tem ' + 'R$' + str(carteira))
print('Com esse dinheiro, você pode comprar US${:.2f}'.format(carteira / 5.32))
print('Você também consegue comprar €{:.2f}'.format(carteira / 6.29))
