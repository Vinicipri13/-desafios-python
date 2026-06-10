from math import radians, sin, cos, tan
angulo = float(input('Digite um angulo em graus: '))
seno = sin(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2F}' .format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2F}' .format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2F}' .format(angulo, tangente))