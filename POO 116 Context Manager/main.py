
# Deste jeito é necessário o CLOSE()
#arquivo = open('abc.txt', 'w')
#arquivo.write('Alguma coisa')
#arquivo.close()

# Desta forma, não é necessário.
#with open('abc.txt', 'w') as arquivo:
#    arquivo.write('Alguma coisa')


class Arquivo:
    def __init__(self, arquivo, modo):
        print('INIT')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('Entrou na classe')
        return self.arquivo

    def __exit__(self):
        print('Saiu da CLASSE')
        self.arquivo.close()

""" with open('abc.txt', 'w') as arquivo:
    arquivo.write('Alguma coisa') """