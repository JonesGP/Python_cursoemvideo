import emoji
cores = {'limpa': '\033[m',
         'vermelha': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m',
         'roxo': '\033[1;35m'}
#MENU
print('{}-={}'.format(cores['amarelo'], cores['limpa']) * 22)
print('{}{:=^44}{}'.format(cores['azul'], ' Desafio 29 ', cores['limpa']))
print('{}-={}'.format(cores['amarelo'], cores['limpa']) * 22)

vel = int(input('{}Qual a velocidade do carro? {}'.format(cores['roxo'], cores['limpa'])))

if vel > 80:
    print(emoji.emojize('{}Você foi multado!!!:disappointed_relieved:\n'
                        'e deverá pagar R${} Reais de multa.'
                        .format(cores['vermelha'], (vel - 80) * 7), use_aliases=True))

else:
    print(emoji.emojize('{}Você esta na velocidade adequada :sunglasses:, '
                        'dirija com cuidado, e tenha um bom dia!{}'.format(cores['verde'], cores['limpa']), use_aliases=True))
print('-----FIM-----')
