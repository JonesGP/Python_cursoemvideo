print('\033[1;33m-=-' * 15)
print('\033[1;34m{:=^45}'.format(' Desafio 33 '))
print('\033[1;33m-=-' * 15)


a = int(input('\033[35mPrimeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))

#Verificando quem é menor

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#Verificando quem é maior

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('\033[32mO menor valor digitado foi {}'.format(menor))
print('\033[36mO maior valor digitado foi {}\033[m'.format(maior))
