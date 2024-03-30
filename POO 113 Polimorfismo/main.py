"""
Polimorfismo é o principio que permite que classes derivadas de uma mesma superclasse
tenham métodos iguais (de mesma assinatura), mas comportamentos diferentes.

Mesma assinatura = Mesma quantidade de tipo de parâmetros.
"""


from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def fala(self, msg): pass

class B(A):
    def fala(self, msg):
        print(f'Falando... B...{msg}')

class C(A):
    def fala(self, msg):
        print(f'Falando... C...{msg}')

b = B()
c = C()

b.fala('Um Assunto')
c.fala('Outro Assunto')