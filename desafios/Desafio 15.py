print('{:=^22}'.format(' Desafio 15 '))
km = float(input('Quantos quilometros você percorreu? '))
dia = float(input('Quantos dia você alugou? '))
p = dia * 60 + (km * 0.15)
print('Você percorreu {}km\n'
      'E usou por {} dias\n'
      'Você vai pagar R${:.2f} reais'.format(km, dia, p))
