velocidade = float(input('Qual a velocidade do carro? '))

if velocidade > 80:
    print('Você excedeu o limite de velocidade de 80km/h')
    print('O valor da sua multa será de R${:.2f}'.format((velocidade - 80) * 7 ))

else:
    print('Parabéns! Você está dirigindo dentro do limite permitido e não será multado(a)')
