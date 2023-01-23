print('\033[33m-=-'*15)

print('{:=^45}'.format(' Desafio 30 '))

print('-=-'*15, '\033[m')

n = int(input('Digite um número qualquer: '))
res = n % 2

if res == 0:
    print('\033[32mO número {} é PAR\033[m'.format(n))
else:
    print('\033[33mO número {} é ÍMPAR\033[m'.format(n))
