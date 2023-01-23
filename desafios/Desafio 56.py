media = 0
idadeHvelho = 0
nomeHvelho = ''
totMMidade = 0
for pess in range(1, 5):
    print('-'*4, ' {} PESSOA '.format(pess), '-'*4)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    media += idade
    
    if sexo == 'M' and idade > idadeHvelho:
        idadeHvelho = idade
        nomeHvelho = nome
    if sexo == 'F' and idade < 20:
        totMMidade += 1


print('A média de idade do grupo é de {} anos.'.format(media / 4))
print('O homem mais velho tem {} anos e se chama {}'.format(idadeHvelho, nomeHvelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totMMidade))
