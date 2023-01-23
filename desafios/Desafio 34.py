print('=-=' * 15)

print('\033[1;33m-=-' * 15)
print('\033[1;34m{:=^45}'.format(' Desafio 34 '))
print('\033[1;33m-=-' * 15)

sal = float(input('\033[1;35mDigite o seu salário: R$'))

if sal <= 1250:
    print('\033[1;32mO seu novo salário é R${:.2f}'.format((sal / 100) * 115))
else:
    print('\033[1;32mO seu novo salário é R${:.2f}'.format((sal / 100) * 110))
print('\033[36mTenha uma bom dia com o seu novo salário!\033[m')

print('=-='* 15)
