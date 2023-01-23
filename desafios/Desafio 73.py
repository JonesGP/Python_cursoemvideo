times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 
'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 
'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 
'Sport Recifi', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 
'Atlético-GO')
pos = 1
cont = 0
for t in times:
    
    if pos < 6:
        if pos == 1:
            print('{:25}'.format('Classificação dos times'), end='')
            print('Os 5 primeiros')
        print(f'{pos:2}ª {t:25}', end='')
        print(f'{pos:2}ª {times[pos-1]}')
    else:
        print(f'{pos:2}ª {t:25}')


    pos += 1
print('-='*30)
print(f'Lista de times do Brasileirão: {times}')
print('-='*30)


print(f'Os 5 primeiros colocados são {times[0:6]}')
print('-='*30)

print(f'Os 4 últimos são {times[-4:]}')
print('-='*30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*30)
print(f'O Chapecoense está na 8ª posição')
print('-='*30)