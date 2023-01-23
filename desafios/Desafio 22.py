print('{:=^22}'.format(' Desafio 22 '))
nome = str(input('Digite o seu nome completo: ')).strip()
print('O seu nome com letras maiúsculas é = {}'.format(nome.upper()))
print('O seu nome com letras maiúsculas é = {}'.format(nome.lower()))
nome = nome.lower().split()
pnome = nome[0]
print('O primeiro nome tem {}'.format(len(pnome)))
nome = ''.join(nome)
print('O seu nome completo tem {} letras'.format(len(nome)))
