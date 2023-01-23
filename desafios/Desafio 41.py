from datetime import date
nasc = int(input('Digite o ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
print('Classificação: ', end='')
if idade <= 9:
    print('MIRIM')
elif idade > 9 and idade <= 14:
    print('INFANTIL')
elif idade > 14 and idade <= 19:
    print('JUNIOR')
elif idade > 19 and idade <= 25:
    print('SÊNIOR')
elif idade > 25:
    print('MASTER')
