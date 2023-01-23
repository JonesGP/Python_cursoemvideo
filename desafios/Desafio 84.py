pessoas = list()
dados = list()
pessPesadas = list()
pessLeves = list()
pesoPesado = pesoLeve = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: Kg ')))
    pessoas.append(dados[:])    #Lembrando que copia se ultiliza [:]

    if len(pessoas) == 1:
        pessPesadas.append(dados[0])
        pessLeves.append(dados[0])
        pesoLeve = pesoPesado = dados[1]

    elif pesoPesado <= dados[1]:
        if pesoPesado == dados[1]:
            pessPesadas.append(dados[0])
        else:
            pessPesadas.clear()
            pessPesadas.append(dados[0])
        pesoPesado = dados[1]

    elif pesoLeve >= dados[1]:
        if pesoLeve == dados[1]:
            pessLeves.append(dados[0])
        else:
            pessLeves.clear()
            pessLeves.append(dados[0])
        pesoLeve = dados[1]
    dados.clear()
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break


print('-='*30)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi {pesoPesado:.1f}Kg. Peso de', end=' ')
for p in pessPesadas:
    print(p, end=' ')
print(f'\nO menor peso foi {pesoLeve:.1f}Kg. Peso de', end=' ')
for p in pessLeves:
    print(p, end=' ')

