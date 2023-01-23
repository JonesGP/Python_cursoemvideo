from random import randint
print('=-'*36)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*36)



cont = 0

while True:
    comput = randint(1, 10)
    n = int(input('Diga um valor: '))
    op = ' '
    while op not in 'PI':
        op = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]

    print(f'Você jogou {n} e o computador {comput}.', end=' ')
    
    soma = comput + n

    if soma % 2 == 0:
        r = 0
        impar = ' deu PAR'
    else:
        r = 1
        impar = ' deu ÍMPAR'
    
    print(f'O total de {soma}{impar}')

    if r == 0 and op == 'P':
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        cont += 1
    elif r == 1 and op == 'I':
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        cont += 1
    else:
        print('Você PERDEU!')
        print('=-'*20)
        print(f'GAME OVER! Você venceu {cont} vezes.')
        break