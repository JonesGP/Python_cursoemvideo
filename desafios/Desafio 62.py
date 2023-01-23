print('Gerador de PA')
print('-='*5)
ptermo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
PA = ptermo
contador = 0
total = 0
op = 10

while op != 0:
    total += op
    while contador <= total:
        print(PA, end=' -> ')
        PA += razao
        contador += 1
    print('PAUSA')
    op = int(input('Quer ver mais quanto? '))
print('FIM')