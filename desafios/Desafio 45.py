from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções: 
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')


print('-=' * 11)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador - 1]))
print('-=' * 11)

if computador == 0: #Computador escolheu Pedra
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('Jogador GANHOU!')
    elif jogador == 2:
        print('Computador GANHOU!')
    else:
        print('Opção inválida! Tente novamente.')

elif computador == 1: #Computador escolheu Papel
    if jogador == 0:
        print('O computador GANHOU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('O jogador GANHOU!')
    else:
        print('Opção inválida! Tente novamente.')
    
elif computador == 2: #Computador escolheu Tesoura
    if jogador == 0:
        print('O jogador GANHOU!')
    elif jogador == 1:
        print('O computador GANHOU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Opção inválida! Tente novamente.')
