class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # Getter
    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

    # Setter
    @nome.setter
    def nome(self, valor):
        self._nome = valor.upper()


    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        
        self._preco = valor