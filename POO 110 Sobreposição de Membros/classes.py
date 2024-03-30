"""
Se utilizar o método super() ele fará com que seja executado
o método da classe superior a de onde ela está sendo chamada
Se chamada no CLIENTEVIP e o método estiver em CLIENTE logo este
será convocado.
"""


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'A classe: {self.nomeclasse}, foi chamada para que {self.nome} fale.')


class Cliente(Pessoa):
    def comprar(self):
        print(f'A classe: {self.nomeclasse}, foi chamada para que {self.nome} compre.')

    def falar(self):
        print('Estou em CLIENTE.')


class ClienteVIP(Cliente):
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade) # Ou super().__init__(nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')

"""     def falar(self):
        Pessoa.falar(self) # Chamará o método falar da classe Pessoa.
        Cliente.falar(self) #chamará o método falar da classe Cliente.
        super().falar() # O super() fará com que o py execute o método da Classe (Pessoa) primeiro.
        print(f'A classe: {self.nomeclasse}, foi chamada para falar qualquer coisa.')
 """
