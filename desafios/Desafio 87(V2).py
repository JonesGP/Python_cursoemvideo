matriz = [[0,0,0], [0,0,0], [0,0,0]]
spar = ster = msegun = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para posição [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
        if matriz[1][c] > msegun:
            msegun = matriz[1][c]
    ster += matriz[l][2]
    print('')
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
print(f'A soma dos valores da terceira coluna é {ster}')
print(f'O maior valor da segunda linha é {msegun}')