salario = float(input('Valor do salário: R$  '))
aumento = salario + (salario * 15 /100)
print('O salário antigo do funcionário era de {} reais e agora é de {:.2f} reais'.format(salario, aumento))