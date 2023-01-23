import random
import emoji
cores = {'limpa': '\033[m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m',
         'roxo': '\033[1;35m'}
print('{}-=-{}'.format(cores['amarelo'], cores['limpa']) * 22)
print('{}{:=^44}{}'.format(cores['azul'], ' Desafio 28 ', cores['limpa']))
print('{}-=-{}'.format(cores['amarelo'], cores['limpa']) * 22)

us = int(input('{}Qual o numero que eu escolhi de 0 a 5? {}'.format(cores['roxo'], cores['limpa'])))
pc = random.randint(0, 5)

if us == pc:
    print(emoji.emojize('{}Você acertou ah mizeravi :sunglasses:'.format(cores['verde']), use_aliases=True))
else:
    print(emoji.emojize('{}Você errou!:astonished: eu disse {}'.format(cores['vermelho'], pc), use_aliases=True))
print('--FIM--')
