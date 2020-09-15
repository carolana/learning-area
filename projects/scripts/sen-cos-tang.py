import math

angulo = float(input('Digite o ângulo desjado: '))
print('Para o ângulo {:.2f} o seno é {:.2f}'.format(angulo, math.sin(math.radians(angulo))))
print('O cosseno é {:.2f}'.format(math.cos(math.radians(angulo))))
print('E a tangente é {:.2f}'.format(math.tan(math.radians(angulo))))
