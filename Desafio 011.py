larg = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))
area = larg * alt
print('Sua parede tem {}m²' .format(area))
tinta = area / 2
print('Você precisa de {:.2f}l de tinta para pintar sua parede' .format(tinta))