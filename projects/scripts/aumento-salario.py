salario = float(input('Digite o valor do salário do funcionário R$ '))

if salario <= 1250.00:
    print('O valor do salário, após o aumento, será de R${}'.format((salario * 0.15) + salario))

else:
    print('O valor do salário, após o aumento, será de R${}'.format((salario * 0.10) + salario))