lista = []
while True:
    n = int(input('Digite um número: '))
    if len(lista) == 0 or n < lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n >= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break

print('-=' * 30)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O 5 faz parte da lista')
else:
    print('O 5 não faz parte da lista')