# @property + @setter - getter e setter no modo Pythônico
# - com getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines não devem ser usados fora da
# classe.

class Caneta:
    def __init__(self, cor):
        # self.cor_tinta = cor
        # private protected
        self._cor = cor  # Esse atributo é para o @property(getter)
        # Nesse caso não tem no init, logo ele deve ser deixado assim.
        self._cor_tampa = None

    @property
    def cor(self):
        return self._cor

    @cor.setter  # É um método que tem self, tem que receber um valor
    def cor(self, valor):
        if valor == 'Rosa':
            raise ValueError('Não aceito essa cor')
        # print('Estou no SETTER', valor)
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor

# def mostrar(caneta):
#     return caneta.cor


caneta = Caneta('Azul')
# Error de atribuição | PARA CASOS EM QUE NÃO SE USOU O GETTER/SETTER
caneta.cor = 'Pink'
caneta.cor_tampa = 'Azul'
# getter -> obter valor
print(caneta.cor)
print(caneta.cor_tampa)
# mostrar(caneta)
