import random
print('{:=^22}'.format(' Desafio 19 '))
al1 = input('Digite o nome do primeiro aluno? ')
al2 = input('Digite o nome do segundo aluno? ')
al3 = input('Digite o nome do terceiro aluno? ')
al4 = input('Digite o nome do quarto aluno? ')
lista = [al1, al2, al3, al4]
esco = random.choice(lista)
print('O aluno escolhido foi {}!'.format(esco))
