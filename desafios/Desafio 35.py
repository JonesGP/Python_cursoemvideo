print('\033[1;33m-=-' * 15)
print('\033[1;34m{:=^45}'.format(' Desafio 35 '))
print('\033[1;33m-=-' * 15)


n1 = float(input('\033[35mPrimeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('\033[32mOs segmentos acima PODEM FORMAR TRIÂNGULO!')
else:
    print('\033[32mOs segmentos acima NÃO PODEM FORMAR TRIÂNGULO!')
print('===FIM===\033[m')
