preço = float(input('Qual o valor do produto que você comprou? R$'))
desconto = int(input('Quanto foi o desconto dado pelo estabelecimento? '))
novo_preço = preço - (preço * desconto /100)
print('O produto que custava R${}, com um desconto de {}%, o novo valor será de R${:.2f} '.format(preço,desconto,novo_preço))