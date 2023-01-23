op = 'S'
cont = soma = maior = menor = 0

while op == 'S':    #Também pode ultilizar o (in 'Ss') para obter o mesmo resultado
    n = int(input('Digite um número: '))

    if cont == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    cont += 1
    soma += n
    op = str(input('Quer continuar? [S/N] ')).strip().upper()[0] #Pega só a primeira letra, ajuda se a pessoa digitar 'sim'

print('Você digitou {} números e a média foi {}'.format(cont, soma / cont))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
