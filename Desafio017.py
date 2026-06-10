import math
oposto = float(input('Valor do cateto oposto: '))
adjacente = float(input('valor do cateto adjacente: '))
hi = math.hypot(oposto, adjacente)
print('O valor da hipotenusa é: {:.2f}' .format(hi))