import random
print('{:=^22}'.format(' Desafio 20 '))
al1 = str(input('Primeito aluno: '))
al2 = str(input('Segundo aluno: '))
al3 = str(input('terceiro aluno: '))
al4 = str(input('Quarto aluno: '))
lista = [al1, al2, al3, al4]
random.shuffle(lista)
print('A ordem de apresentação será ')
print(lista)
