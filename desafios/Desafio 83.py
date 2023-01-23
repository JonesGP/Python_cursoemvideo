expressao = str(input('Digite a expressão: '))
pilha = []
for c in expressao:
    if c == '(':
        pilha.append(c)
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão válida! ')
else:
    print('Expressão inválida!')
 