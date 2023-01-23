while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*35)
    if n < 0:
        break
    
    for cont in range(1, 11):
        mult = n * cont
        print(f'{n} x {cont:2} = {mult}')

    print('-'*35)
print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')
