from datetime import date
atual = date.today().year

nasc = int(input('Digite o ano de nascimento: '))
sexo = int(input('''[1] para masculino
[2] para feminino
Digite o seu sexo: '''))
idade = atual - nasc

if sexo == 1:
    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
    if idade == 18:
        print('Já está na hora de se alistar!')
    elif idade < 18:
        print('Ainda falta {} anos para seu alistamento!'.format(18 - idade))
        print('seu alistamento será em {}'.format(atual + (18 - idade)))
    elif idade > 18:
        print('Ja passou {} anos para seu alistamento!'.format(idade - 18))
        print('Seu alistamento foi em {}'.format(atual - (idade - 18)))
elif sexo == 2:
    print('Você não é obrigada a se alistar')
else:
    print('Opção invalida, tente novamente')
