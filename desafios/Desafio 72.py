lista = ('zero', 'um', 'dois', 'três', 'quatro', 
        'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'catorze', 'quinze', 
        'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

n = -1
op = ' '
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: ')) 
        if n < 0 or n > 20:
            print('Tente novamente. ', end='')
        if 0 <= n <= 20:
            break    
    
    print(f'Você digitou {lista[n]}')
    while op not in 'SN':
        op = str(input('Quer continuar: [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
    n = -1
    op = ' '
print('Fim do programa!')
