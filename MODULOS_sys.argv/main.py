# sys.argv - Executando arquivos com argumentos no sistema
# Fonte = Fira Code

import sys

print(sys.argv)

argumentos = sys.argv
qtd_argumentos = len(argumentos)

print(qtd_argumentos)

if qtd_argumentos <= 1:
    print('você não passou argumentos.')
else:
    try:
        print(f'Você passou os argumentos: {argumentos[1:]}')
        print(f'Faça alguma coisa com {argumentos[1]}')
        print(f'Faça outra coisa com {argumentos[2]}')
        print(f'Faça outra coisa com {argumentos[3]}')
    except IndexError:
        print('Faltam argumentos')
