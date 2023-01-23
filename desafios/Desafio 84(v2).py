listapessoas = []   #Lista completa de pessoas.
pessoa = []         #Lista temporária para cada pessoa que será adicionada na lista principal.
maiorPeso = menorPeso = 0      #Declara as variáveis para guarda o maior o menor peso e o total de pessoas.
while True:         #Laço programa principal
    pessoa.append(str(input('Nome: ')))     #Pega o nome da pessoa e adiciona na lista temporária.
    pessoa.append(float(input('Peso: ')))   #Pega o peso da pessoa e adiciona na lista temporária.
    if len(listapessoas) == 0:                     #Torna o primeiro peso como maior e menor.
        menorPeso = maiorPeso = pessoa[1]
    elif maiorPeso < pessoa[1]:             #Se o maior peso for menor que o peso cadastrado atualmente.
        maiorPeso = pessoa[1]               #Adiciona o peso atual na variável maiorPeso.
    elif menorPeso > pessoa[1]:             #Se o menor peso for maior que o peso cadastrado atualmente.
        menorPeso = pessoa[1]               #Adiciona o peso atual na variável menorPeso.
    
    listapessoas.append(pessoa[:])      #Pega a lista temporária e adiciona la lista principal.
    pessoa.clear()                      #Limpa a lista temporária para receber novos dados

    op = ' '                            #Variável para guardar a opção do jogador.
    while op not in 'SN':               #Laço para pergunta se a pessoa que continuar.
        op = str(input('Quer continuar? [S/N] ')).upper().split()[0]    #Faz a pergunta já formantando-a para dixa-la pronta para condição.
    if op == 'N':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(listapessoas)}')  #Escreve na tela a quantidade de pessoas cadastradas.
print(f'O maior peso foi de {maiorPeso:.1f}Kg. Peso de', end=' ')   #Escreve na tela o maior peso.
for p in listapessoas:              #Lista para pegar as lista temporária de cada pessoa cadastrada.
    if p[1] == maiorPeso:           #Verifica se o peso da pessoa da lista atual é igual ao maior peso.
        print(f'[{p[0]}]', end=' ') #Escreve na tela o nome da pessoa.
print(f'\nO menor peso foi de {menorPeso:.1f}Kg. Peso de', end=' ') #Escreve na tela o menor peso.
for p in listapessoas:              #Lista para pegar a lista temporária de cada pessoa cadastrada.
    if p[1] == menorPeso:           #Verifica se o peso da pessoa da lista atual pe igual ao maior peso.
        print(f'[{p[0]}]', end=' ') #Escreve na tela o nome da pessoa.
