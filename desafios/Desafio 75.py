numeros =  (int(input('Digite um número: ')), 
            int(input('Digite outro número: ')),
            int(input('Digite mais um número: ')), 
            int(input('Digite o ultimo número: ')))
print(f'Você digitou os valores {numeros}')

if 9 in numeros:
    print(f'O valor 9 apareceu {numeros.count(9)} vezes')
else:
    print('Não ha nenhum nove')

if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição')
else:
    print('Não tem nenhum 3')

print('Os valores pares digitados foram ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')