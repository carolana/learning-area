salario = float(input('Quanto é seu salário atualmente? R$ '))
reajuste = float(input('E quanto foi o reajuste deste ano? '))
novo_salario = (reajuste / 100) + 1
print('Com o reajuste de {}%, seu salário que antes era R${}, passará a ser R${:.2f}'.format(reajuste, salario, (salario * novo_salario)))