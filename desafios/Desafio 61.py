print('Gerador de PA')
print('-='*5)
contador = 0
op = 'S'

while op != 'N':
    ptermo = int(input('Primeiro termo: '))
    razao = int(input('Razão da PA: '))
    while contador < 10:
        print(ptermo, end=' -> ')
        ptermo += razao
        contador += 1
    
    contador = 0
    op = str(input('Quer continuar: [S/N] ')).strip().upper()
print('FIM')