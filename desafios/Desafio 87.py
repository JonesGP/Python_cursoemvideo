matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = coluna3soma = maiorlinha2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f'Digite um numero para posição [{l}, {c}]: '))
        matriz[l][c] = valor

        if valor % 2 == 0:
            somapares += valor
        if c == 2:
            coluna3soma += valor
        if l == 1:
            if c == 0:
                maiorlinha2 = valor
            if maiorlinha2 < valor:
                maiorlinha2 = valor
        valor = 0

print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print('')
print('-=' * 30)
print(f'A soma de todos os valores pares é {somapares}.')
print(f'A soma de todos os valores da coluna 3 é {coluna3soma}.')
print(f'O maior valor da segunda linha é {maiorlinha2}.')