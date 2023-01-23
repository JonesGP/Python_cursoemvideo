frase = str(input('Digite uma frase: ')).strip().upper()
separada = frase.split()
junta = ''.join(separada)
inverso = ''
for letra in range(len(junta) - 1, -1, -1):
    inverso += junta[letra]
print('O inverso de {} é {}.'.format(junta, inverso))
if inverso == junta:
    print('Temos um palíndromo.')
else:
    print('Nao temos um palíndromo.')

frase = str(input('Digite uma frase: ')).strip().upper()
separada = frase.split()
junta = ''.join(separada)
inverso = junta[::-1]
print('O inverso de {} é {}.'.format(junta, inverso))
if inverso == junta:
    print('Temos um palíndromo.')
else:
    print('Nao temos um palíndromo.')
