
print('{:=^22}'.format(' Desafio 17 '))
'''
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
'''

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do vateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
