from random import randint
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)

cont = 0
while True:
    jogador = int(input('Diga um número: '))

    op = ' '
    while op not in 'PI':
        op = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]

    comput = randint(1, 10)
    soma   = jogador + comput
    print('-'*40)
    print(f'Você jogou {jogador} e o computador {comput}. Total de {soma} deu ', end='')
    print('PAR' if soma % 2 == 0 else 'ÍMPAR')
    print('-'*40)

    if soma % 2 == 0:
        if op == 'P':
            print('Você GANHOU, PARABÉNS!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    else:
        if op == 'I':
            print('Você GANHOU, PARABÉNS')
            cont += 1
        else:
            print('Você PERDEU!')
            break
print('=-'*20)
print(f'GAME OVER! Você venceu {cont} vezes.')