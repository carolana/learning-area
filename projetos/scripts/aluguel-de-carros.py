dias_usados = int(input('Quanto dias alugado? '))
km_rodados = float(input('Quantos km foram percorridos? '))
print('O total a pagar é R${:.2f}'.format((dias_usados * 60) + (km_rodados * 0.15)))