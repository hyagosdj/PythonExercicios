from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self): 
        return self._name

    @name.setter
    @abstractmethod
    def name(self, name): ... 
        

# Sobreposição do método init/name.
class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name) #aqui é onde realmente será chamado a inicialização da name.
        print('Essa classe é inútil')
        
    # Esse caso é para quando você precisa utilizar o getter (@property) e o Sobrescrever o Setter da classe Foo que está herdando da classe abstrata (AbstractFoo) por exemplo.
    @AbstractFoo.name.setter 
    def name(self, name):
        self._name = name

foo = Foo('Bar')
print(foo.name)