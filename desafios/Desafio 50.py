soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}ª valor : '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
if cont == 0:
    print('Não foi digitado nenhum número par!')
elif cont == 1:
    print('Você informou {} número par e a soma é ele mesmo {}.'.format(cont, soma))
else:
    print('Você informou {} números pares e a soma entre eles é {}.'.format(cont, soma))
