preco = float(input('Preço do produto: R$ '))
desconto = preco - (preco * 5 / 100)
print('O valor do produto com desconto aplicado é de {:.2f} Reais'.format(desconto))