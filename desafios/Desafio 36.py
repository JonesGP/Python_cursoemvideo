print('\033[1;35m-=-' * 15)
print('\033[1;33m-=-' * 15)
print('\033[1;34m{:=^45}'.format(' Desafio 36 '))
print('\033[1;33m-=-'* 15)


valcas = float(input('\033[36mQual o valor da casa: R$'))
sal = float(input('Qual o seu salário: R$'))
anos = int(input('Em quantos anos pretende parcelar: '))

valpres = valcas / (anos * 12) #Quanto custa a prestação da casa
salpres = sal / 100 * 30       #Ver se o salário passa de 30% do permitido

print('\033[37mPara pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valcas, anos, valpres))

if valpres > salpres:
    print('\033[1;31mSeu empréstimo foi NEGADO!')
elif valpres <= salpres:
    print('\033[1;32mSeu empréstimo pode ser APROVADO!')

print('Tenha um bom dia')
print('\033[1;35m-=-\033[m' * 15)