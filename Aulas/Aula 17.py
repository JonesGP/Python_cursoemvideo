num = [2, 5, 9, 1]
num[2] = 3      #Muda o valor da posição 2
num.append(7)   #Adiciona um(7) valor ao final da lista
num.insert(2, 0)#Adiciona o valor(0) na posição (2) e empurra os outros valores pra frente

num.sort()      #Vai ordenar a lista
num.sort(reverse=True)  #vai ordenar a lista ao contrário

num.pop()       #Normalmente utilizado para remover o último elemento da lista
num.pop(2)      #Mas pode ser usado para remover o valor que você quiser
num.remove(2)   #Este método varre do inicio até remover o valor selecionado uma vez, no caso o primeiro valor que você escolheu para excluir

if 4 in num:    #Se 4 estiver na lista ele remove o 4, senão ele escreve que 'Não achou o número 4'
    num.remove(4)
else:
    print('Não achei o número 4')

valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...')

for c, valor in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')

lista = []
for cont in range(0, 5):
    lista.append(int(input('Digite um valor: ')))

a = [2, 3, 4, 7]
b = a       #CUIDADO Neste caso o python está fazendo uma ligação da variável (b) com (a), então toda modificação com (b) também modificará (a)
b = a[:]    #Cria uma copia de (a) dentro do (b)
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')