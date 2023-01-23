print('{:=^22}'.format(' Desafio 24 '))
"""
nome = str(input('Digite o nome da sua cidade: ')).lower().split()
nome = nome[0]
print('Sua cidade tem santo? {}'.format('santo' in nome))
"""
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].lower() == 'santo')
