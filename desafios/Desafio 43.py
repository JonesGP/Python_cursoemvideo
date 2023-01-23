peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso /(altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('ABAIXO DO PESO')

elif imc > 18.5 and imc <= 25:
    print('PESO IDEAL')

elif imc > 25 and imc <= 30:
    print('SOBREPESO')

elif imc > 30 and imc <= 40:
    print('OBESIDADE')
    
elif imc > 40:
    print('OBESIDADE MÓRBIDA')
