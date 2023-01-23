listalunos = []
aluno = []
while True:
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    aluno.append((aluno[1] + aluno[2]) / 2)
    listalunos.append(aluno[:])
    aluno.clear()
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
print('-=' * 15)
print(f'{"No":<3} {"NOME":<10} {"MÉDIA":^5}')
print('-' * 30)
for c in range(1, len(listalunos) + 1):
    print(f'{c:<3} {listalunos[c - 1][0]:<10} {listalunos[c - 1][3]:>5.1f}')
op2 = 0
while True:
    print('-' * 30)
    op2 = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if op2 == 999:
        break
    if op2 <= len(listalunos):
        print(f'Notas de {listalunos[op2 - 1][0]} são {listalunos[op2 - 1][1:3]}')
    else:
        print('Aluno não encotrado!')