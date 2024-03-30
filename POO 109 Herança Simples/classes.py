"""
Quem herda em Herança é sempre as filhas(Cliente e Aluno),
Logo quem é a Mãe ou Superclasse (Pessoa) é a primeira que define os métodos.
"""


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'A classe: {self.nomeclasse} foi chamada')
        print(f'{self.nome} está falando...')

class Cliente(Pessoa):
    def comprar(self):
        print(f'A classe {self.nomeclasse} foi chamada para que o(a): {self.nome} compre.')

    
class Aluno(Pessoa):
    def estudar(self):
        print(f'A clase: {self.nomeclasse} foi chamada para que o(a): {self.nome} estude.')