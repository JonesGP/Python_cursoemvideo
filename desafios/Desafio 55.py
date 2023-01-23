maior = 0
menor = 0
for pessoas in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(pessoas)))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi {}Kg\nO menor peso foi {}Kg'.format(maior, menor))


ma = 0   #maior peso
mn = 999 #menor peso
for p in range(1, 6):
    pes = float(input('Peso da {}ª pessoa: '.format(p)))
    if pes > ma: #Ver quem é o maior peso a cada pergunta
        ma = pes
    if pes < mn: #Ver quem é o menor peso a cada pergunta
        mn = pes
print('O maior peso foi {}Kg\nO menor peso foi {}Kg'.format(ma, mn))
