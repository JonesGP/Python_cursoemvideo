print('\033[33m-=-'*15)
print('\033[36m{:=^45}'.format(' Desafio 31 '))
print('\033[33m-=-'*15)
d = int(input('\033[36mQual a distância da sua viajem em km: '))
print('\033[35mVocê vai viajar {}km'.format(d))
if d > 200:
    print('\033[32mVocê devera pagar R${:.2f} Reais\033[m'.format(d * 0.45))
else:
    print('\033[31mVocê deverá pagar R${:.2f} Reais\033[m'.format(d * 0.50))
