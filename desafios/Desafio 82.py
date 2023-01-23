lista = []
listapares = []
listaimpares = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        listapares.append(n)
    else:
        listaimpares.append(n)
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
print('-='*30)
print(f'A lista completa é {lista}')
print(f'A lista de Pares é {listapares}')
print(f'A lista de Ímpares é {listaimpares}')