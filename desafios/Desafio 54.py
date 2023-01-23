from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pessoas in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoas)))
    idade = atual - nasc
    if idade < 18:
        menor += 1
    else:
        maior += 1
print('Ao todo tinvemos {} pessoas mariores de idade\ne também tinvemos {} pessoas menores de idade'.format(maior, menor))
