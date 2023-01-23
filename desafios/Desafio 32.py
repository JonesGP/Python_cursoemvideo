print('===' * 15)
print('\033[1;33m-=-' * 15)
print('\033[1;35m{:=^45}'.format(' Desafio 32 '))
print('\033[1;33m-=-' * 15)

from datetime import date
ano = int(input('\033[36mQue ano quer analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:  #se for digitado 0 será convertido para o ano atual
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[32mO ano {} é BISSEXTO\033[m'.format(ano))

else:
    print('\033[31mO ano {} NÂO é BISSEXTO\033[m'.format(ano))

print('===' * 15)
