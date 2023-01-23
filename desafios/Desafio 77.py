palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 
            'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar', 
            'Mercado', 'Programador', 'Futuro')

for p in palavras:  # Para cada palatra{p} dentro da Tupla{palavras}
    print(f'\nNa palavra {p.upper()} temos ', end='') # Escreva palavra

    for letra in p: # Para cada letra{letra} de cada palavra{p}
        if letra.lower() in 'aeiou':    
            print(letra, end=' ')