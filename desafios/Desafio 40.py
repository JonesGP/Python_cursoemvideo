nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print('A média do aluno é {:.1f}'.format(media))

if media >= 7:
    print('Você foi APROVADO')
elif media >= 5 and media < 6.9:
    print('Você ficou de RECUPERAÇÃO')
else:
    print('Você foi REPROVADO')
