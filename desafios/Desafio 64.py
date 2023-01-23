op = cont = soma = 0
op = int(input('Digite um número [999 para parar]: '))
while op != 999:
    soma += op
    cont += 1
    op = int(input('Digite um número [999 para parar]: '))
    
print('Você digitou {} numeros e a soma entre eles foi {}.'.format(cont, soma))
