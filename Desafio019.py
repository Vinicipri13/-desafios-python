from random import choice
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo alunos: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
alunos = (aluno1, aluno2, aluno3, aluno4)
sorteado = choice(alunos)
print('Entre os alunos {}, {}, {}, {}. O aluno que deverá apagar o quadro é: {}' .format(aluno1, aluno2, aluno3, aluno4, sorteado))