num = int(input('Digite um número: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;32m', c, '\033[m', end='')
        cont += 1
    else:
        print('\033[1;31m', c, '\033[m', end='')
print('\n\033[1;35mO número {} foi divisível {} vezes'.format(num, cont))
if cont == 2:
    print('\033[1;32mE por isso ele é primo!\033[m')
else:
    print('\033[1;31mE por isso ele não é primo!\033[m')
