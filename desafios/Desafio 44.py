print('{:=^44}'.format(' Lojas Guanabara '))
preco = float(input('Qual o preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] À vista dinheiro/cheque
[2] À vista no cartão
[3] Em até 2x no cartão
[4] 3x ou mais no cartão''')
op = int(input('Sua opção: '))
if op == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, (preco / 100) * 90))
elif op == 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, (preco / 100) * 95))
elif op == 3:
    print('Sua compra de R${:.2f} em 2x de R${:.2f} sem juros.'.format(preco, preco / 2))
elif op == 4:
    par = int(input('Quantas parcelas: '))
    print('Sua compra de R${:.2f} em {}x de R${:.2f} com juros vai custar R${:.2f}'.format(preco, par, (preco / 100 * 120) / par, preco / 100 * 120))
else:
    print('Opção invalida tente novamente!')
