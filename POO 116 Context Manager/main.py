
# Deste jeito é necessário o CLOSE()
# Por extenso:
#arquivo = open('abc.txt', 'w')
#arquivo.write('Alguma coisa')
#arquivo.close()

# Abreviado:
# Desta forma, não é necessário.
#with open('abc.txt', 'w') as arquivo:
#    arquivo.write('Alguma coisa')


# class Arquivo:
#     def __init__(self, arquivo, modo):
#         print('INIT')
#         self.arquivo = open(arquivo, modo)

#     def __enter__(self):
#         print('Entrou na classe')
#         return self.arquivo

#     def __exit__(self):
#         print('Saiu da CLASSE')
#         self.arquivo.close()

""" with open('abc.txt', 'w') as arquivo:
    arquivo.write('Alguma coisa') """

class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('ABRINDO ARQUIVO')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print('FECHANDO ARQUIVO')
        self._arquivo.close()

        # raise class_exception(*exception_.args).with_traceback(traceback_)

        # print(class_exception)
        # print(exception_)
        # print(traceback_)
        
        exception_.add_note('Minha nota.')

        # raise ConnectionError('Não deu para conectar.')

        # return True # Tratei a exceção

# instancia = MyOpen('aulaContexManager.txt', 'w')

with MyOpen('aulaContexManager.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n', 123)
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)