# Context Manager com função - Criando e Usando gerenciadores de contexto

from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
    except Exception as e:
        print('Ocorreu erro:', e)
    finally:
        print('Fechando arquivo')
        arquivo.close()



with my_open('AulaContext.txt', 'w') as arquivo:
    arquivo.write('Linha1\n')
    arquivo.write('Linha2\n', 123)
    arquivo.write('Linha3\n')
    print('WITH', arquivo)