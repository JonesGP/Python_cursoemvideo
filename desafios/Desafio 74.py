# max informa o maior numero
# min informa o menor numero

from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram: ', end='')
for n in num:
    print(f'{n} ', end='')
print(f'\nO maior valor é {max(num)}')
print(f'O menor valor é {min(num)}')

