print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$'))
cont50 = cont20 = cont10 = cont1 = 0
while True:
    if valor >= 50:
        valor -= 50
        cont50 += 1
    elif valor >= 20 and valor < 50:
        valor -= 20
        cont20 += 1
    elif valor >= 10 and valor < 20:
        valor -= 10
        cont10 += 1
    elif valor > 0 and valor < 10:
        valor -= 1
        cont1 += 1
    elif valor == 0:
        break
    print('C')
    print(valor)
print(f'''Total de {cont50} de R$50
Total de {cont20} de R$20
Total de {cont10} de R$10
Total de {cont1} de R$1''')