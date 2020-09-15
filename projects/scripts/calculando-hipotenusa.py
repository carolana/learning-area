from math import hypot

caop = float(input('Qual o cateto oposto? '))
caadj = float(input('Qual o cateto adjacente? '))
hipotenusa = hypot(caop, caadj)
print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))