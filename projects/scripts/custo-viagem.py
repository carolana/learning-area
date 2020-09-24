distancia = float(input('Quantos km você percorreu? '))

if distancia <= 200:
    print('Para uma distância de {}km, o preço da passagem será de R${}'.format(distancia, (distancia * 0.50)))
    
else:
    print('Para uma distância de {}km o preço da passagem é R${}'.format(distancia, (distancia * 0.45)))