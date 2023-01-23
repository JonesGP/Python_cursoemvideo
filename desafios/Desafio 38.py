n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O número {} é maior.'.format(n1))
elif n1 < n2:
    print('O número {} é maior.'.format(n2))
else:
    print('Os dois números são iguais.')
