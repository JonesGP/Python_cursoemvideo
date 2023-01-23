lista = []
for cont in range(0, 5):        #Laço para adicionar valores a lista(lista)
    lista.append(int(input(f'Digite um valor para a posiçao {cont}: ')))    #Pega os valores digitados e os coloca na lista (lista)
    if cont == 0:               #No primeiro laço o (maior) e o (menor) é igual a (lista na posição (cont)
        maior = menor = lista[cont]
    else:                       #Define quem é o maior e o menor
        if lista[cont] > maior: #Define o maior
            maior = lista[cont]
        if lista[cont] < menor: #Define o menor
            menor = lista[cont]

print('-=' * 30)
print(f'Você digitou os valores {lista}')   #Escreve os valore da lista (lista)

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for pos, n in enumerate(lista): #Varre a lista a procura da posição do maior
    if n == maior:              #Se o número(n) for igual ao maior então a posição(pos) é escrita na tela
        print(f'{pos}...', end=' ')

print()

print(f'O menor valor digitado foi {menor} nas posições ', end='')
for pos, n in enumerate(lista): #Varre a lista a procura da posição do menor
    if n == menor:              #Se o número(n) for igual ao menor então a posição(pos) é escrita na tela
        print(f'{pos}...', end=' ')


