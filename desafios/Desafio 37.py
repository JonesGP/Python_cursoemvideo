print('\033[1;33m-=-' * 15)
print('\033[1;36m{:=^45}'.format(' Desafio 37 '))
print('\033[1;33m-=-' * 15)

n = int(input('Digite um número inteiro: '))

print('''\033[1;35mEscolha uma opção:
[1] para binário
[2] para octal
[3] para hexadecimal''')
op = int(input('\033[1;36mSua opção: '))

if op == 1:
    print('\033[1;32m{} convertido para BINÁRIO é {}'.format(n, bin(n)[2:]))
elif op == 2:
    print('{} convertido para OCTAL é {}'.format(n, oct(n)[2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(n, hex(n)[2:]))
else:
    print('\033[1;31mOpção inválida, tente novamente.\033[m')
    
print('\033[1;35m=' * 40)
