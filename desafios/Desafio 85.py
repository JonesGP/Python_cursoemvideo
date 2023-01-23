lista = [[], []]
numero = 0
for c in range(1, 8):
    numero = int(input(f'Digite o {c}ª número: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)
lista[0].sort()
lista[1].sort()
print('-=' * 30)
print(f'Os valores pares digitados foram: ', lista[0])
print(f'Os valores ímpares digitados foram: ', lista[1])
