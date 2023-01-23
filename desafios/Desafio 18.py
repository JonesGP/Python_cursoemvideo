import math
print('{:=^22}'.format(' Desafio 18 '))
an = float(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, sen))
coss = math.cos(math.radians(an))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, coss))
tan = math.tan(math.radians(an))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an, tan))
