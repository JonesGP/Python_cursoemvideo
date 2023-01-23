'''
teste = list()          #Cria a lista teste.
teste.append('Jones')   #Adiciona o 'Jones' a lista teste.
teste.append(40)        #Adiciona o 40 a lista teste.
galera = list()         #Cria a lista galera.
galera.append(teste)    #Esta linha esta criando uma ligação das duas listas teste e galera.
galera.append(teste[:]) #Esta é a forma correta de fazer uma copia de um lista!.
teste[0] = 'Maria'      #Troca o item [0] da lista teste e adiciona 'Maria'.
teste[1] = 22           #Troca o item [1] da lista teste e adiciona 22.
galera.append(teste)    #Tome CUIDADO com este tipo de atribuição.
galera.append(teste[:]) #Esta é a forma correta de fazer uma copia de uma lista!.
print(teste)            
'''

'''
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])

for p in galera:
    print(p)

for p in galera:
    print(p[0])

for p in galera:
    print(p[1])

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
'''

galera = list()                             #Cria a lista galera.
dado = list()                               #Cria a lista dado.
totmaior = totmenor = 0                     #Cria as variáveis que vão guardar os valores de maior e menor de idade.
for c in range(0,3):                        #Cria um laço de 0 a 2 ou 1 a 3 para pegar as informações e adicionar na lista galera.
    dado.append(str(input('Nome: ')))       #Adiciona a informaçã o Nome a lista dado.
    dado.append(int(input('Idade: ')))      #Adiciona a informação idade a lista dado.
    galera.append(dado[:])                  #Cria uma copia de dado e adiciona ao final da lista galera.
    dado.clear()                            #Limpa a lista dado para poder adicionar outros dados na mesma posição do anterior.
print(galera)                               #Escreve o conteudo de galera.

for p in galera:                            #Laço que vai pegar cada lista dentro de galera e em seguida irá fazer as verificações de quem é maior e menor.
    if p[1] >= 21:                          #Verifica se p[1] é maior ou igual a 21.
        print(f'{p[0]} é maior de idade.')  #Escreve o valor de p[0].
        totmaior += 1                       #Variável de contador adiciona mais um valor.
    else:                                   #Se acondiçã anterior não for verdadeira executa essa.
        print(f'{p[0]} é menor de idade.')  #Escreve o valor de p[0]
        totmenor += 1                       #Variável de contador adiciona mais um valor.
print(f'Temos {totmaior} maiores e {totmenor} menores de idade.')   #Escreve o resultado do programa.

