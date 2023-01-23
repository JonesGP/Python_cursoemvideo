n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
op = 0
while op != 5:
    print('''
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA
    ''')
    op = int(input('Sua opção: '))
    if op == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif op == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
    elif op == 3:
        if n1 > n2:
            print('O maior valor é {}'.format(n1))
        elif n2 < n2:
            print('O maior valor é {}'.format(n2))
        else:
            print('Os dois números são iguais')
    elif op == 4:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digige o segundo valor: '))
    elif op == 5:
        print('Até a proxima!')
    else:
        print('Opção inválidada!. Tente novamente.')
print('FIM')