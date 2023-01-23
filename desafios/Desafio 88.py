from random import randint
from time import sleep
print('-' * 30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-' * 30)
todosjogos = []
jogo = []
numj = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'=-=-= SORTEANDO {numj} JOGOS =-=-=')
for lista in range (1, numj + 1):
    while True:
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
        if len(jogo) == 6:
            break
    jogo.sort()
    print(f'Jogo {lista:^2}: {jogo}')
    todosjogos.append(jogo[:])
    jogo.clear()
    sleep(1)
print('-=' * 5, ' < BOA SORTE! > ', '-=' * 5)
