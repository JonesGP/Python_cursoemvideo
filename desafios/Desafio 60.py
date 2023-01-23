from math import factorial
'''
n = int(input('Digite o número para calcular seu Fatorial: '))
f = factorial(n)
print('O Fatorial de {} é {}.'.format(n, f))
'''
'''
n = int(input('Digite o número para calcular o Fatorial: '))
quantidade = n
#f = factorial(n)
f = 1
print('{}! = '.format(n), end='')
while quantidade > 0:
    print('{}'.format(quantidade), end='')
    print(' x ' if quantidade > 1 else ' = ', end='')
    f = f * quantidade
    quantidade -= 1
    #if quantidade > 1:
    #    print(' x ', end='')
    #else:
    #    print(' = {}'.format(f), end='')
print('{}'.format(f))
'''

n = int(input('Digite o número para calcular seu Fatorial: '))
f = 1
print('Calculando {}! = '.format(n), end='')
for c in range(n, 0, -1):
    print('{}'.format(c),end='')
    f *= c
    print(' x ' if c > 1 else ' = {}'.format(f), end='')
