valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} valores')
valores.sort(reverse = True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O número 5 está na lista.')
else:
    print('Não foi encontrado o número 5 na lista')