class TaErradoError(Exception):
    ...

class OutroError(Exception):
    ...


def testar():
    excessao = TaErradoError('A', 'B', 'C')
    excessao.add_note('Olha a nota 1')
    excessao.add_note('Você errou isso')
    raise excessao

try:
    #1/0
    testar()
except (TaErradoError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    #print(f'Erro: {error}')
    excessao = OutroError('Vou lançar novamente')
    excessao.__notes__ = error.__notes__.copy()
    excessao.add_note('Mais uma nota')
    raise excessao from error