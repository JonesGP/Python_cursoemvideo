listanum = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in listanum:
        listanum.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
print('-=' * 30)
listanum.sort()
print(f'Você digitou os valores {listanum}')