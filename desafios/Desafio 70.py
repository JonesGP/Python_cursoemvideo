print('-'*40)
print('{:-^40}'.format(' LOJA SUPER BARATÃO '))
print('-'*40)
tot = totmil = pbarato = 0
nomepb = ''
while True:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    
    tot += preco
    if tot == preco or preco < pbarato:
        pbarato = preco
        nomepb = nome
    if preco > 1000:
        totmil += 1


    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${tot:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomepb} que custa R${pbarato:.2f}')