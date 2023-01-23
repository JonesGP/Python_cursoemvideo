# Com duas Tuplas
print('-'*33)
print('{"LISTAGEM DE PREÇOS":^33}')
print('-'*33)
lista = ('Lápis', 'Borracha', 'Caderno', 'Estojo', 'Transferidor', 'Compasso', 'Mochila', 'Canetas', 'Livro')
preco = ('R$', 1.75, 2, 15.90, 25, 4.20, 9.99, 120.30, 22.30, 34.90)
contPreco = 1
for l in lista:
    print(f'{l:.<20} {preco[0]} {preco[contPreco]:>7.2f}')
    contPreco += 1 

#Com uma Tupla
print('-'*33)
print('{"LISTAGEM DE PREÇOS":^33}')
print('-'*33)
listagem = ('Lápis', 'Borracha', 'Caderno', 'Estojo', 'Tranferidor', 'Compasso', 'Mochila', 'Canetas', 'Livro', 'R$', 
            1.75, 2, 15.90, 25, 4.20, 9.99, 120.32, 22.30, 34.90)
contListagem = 10
for listage in range(0, 9):
    print(f'{listagem[listage]:.<20} {listagem[9]} {listagem[contListagem]:>7.2f}')
    contListagem += 1

#Método Par ou Ímpar
print('-'*33)
print('{"LISTAGEM DE PREÇO":^33}')
print('-'*33)
lista2 = (  'Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Tranferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
for l2 in range(0, len(lista2)):
    if l2 % 2 == 0:
        print(f'{lista2[l2]:.<22}', end='')
    else:
        print(f'R${lista2[l2]:>7.2f}')
print('-'*33)