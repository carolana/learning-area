temperatura = float(input('Qual a temperatura em °C? '))
print('A temperatura {}°C corresponde a {:.2f}°F e {:.2f}°K'.format(temperatura,(temperatura * 1.8 + 32),(temperatura + 273.15)))