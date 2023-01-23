#Tuplas são imutáveis




lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
for cont2 in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont2]}')

for cont in range (0, len(lanche)):
    print(lanche[cont])

for comida in lanche:
    print(f'Eu vou comer {comida}')

for pos, comida2 in enumerate(lanche):
    print(f'Eu vou comer {comida2} na posição {pos}')

print(sorted(lanche))   #Mostra o conteudo de lanche em ordem

a = (2, 5, 4)           #Tupla
b = (5, 8, 1, 2)        #Tupla
c = a + b
print(c)
print(c.count(2))       #Conta quantos 2 tem na tupla
print(c.index(4))       #Mostra a posição do 4 na tupla
print(c.index(2, 2))    #Mostra a posição do 2 apartir do primeiro 5

pessoa = ('Gustavo', 39, 'M', 99.88) #Pode-se colocar qualquer coisa dentro de tuplas
print(pessoa)

del(pessoa) #Deleta qualquer coisa dentro do Python como Exemplo a variável pessoa