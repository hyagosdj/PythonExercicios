"""

O abstractmethod serve para isolar um método e torná-o abstrato e utiliza-se somente suas funcionalidades.

"""

from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def falar(self):
        pass

class B(A):
    def falar(self):
        print('falando... B...')
# Exemplo no primeiro caso a funcionalidade falar será cobrada e utilizada corretamente
a = A()
a.falar()

# Exemplo do segundo caso a funcionalidade falar será cobrada, porém não poderá ser utilizada.
b = B()
a.falar()
