par = impar = 0
n = 0
print('''
Seja bem vindo:
[ s ] para sair
''')

while n != 's':
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1


print('Você digitou {} número pares e {} número ímpares.'.format(par, impar))
print('Acabou')