print('{:=^22}'.format(' Desafio 27 '))
n = str(input('Digite o seu nome: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome) - 1]))
