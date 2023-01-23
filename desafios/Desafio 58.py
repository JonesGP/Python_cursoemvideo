from random import randint
computador = randint(0, 10)
pessoa = -1
palpites = 0
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi? ''')
while pessoa != computador:
    pessoa = int(input('Qual o seu palpite? '))
    if pessoa < computador:
        print('Mais... Tente mais uma vez.')
    elif pessoa > computador:
        print('Menos... Tente mais uma vez.')
    palpites += 1
print('Acertou com {} tentativas. Parabéns!'.format(palpites))


compu = randint(0, 10)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == compu:
        acertou = True
    else:
        if jogador < compu:
            print('Mais... Tente mais uma vez: ')
        elif jogador > compu:
            print('Menos... Tente mais uma vez: ')
print('Acertou com {} tentativas. Parabéns! ')
