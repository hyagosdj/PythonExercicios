# Funções decoradoras e decoradores com classes

# Essa define o que irá ocorrer.
def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr

def adiciona_repr(cls): # Esta chama o que foi definido e retornar o que foi inserido.
    cls.__repr__ = meu_repr
    return cls

def meu_planeta(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)

        if 'Terra' in resultado:
            return 'Você está em casa'
        return resultado
    return interno

# Isso não precisa mais.
# class MyReprMixin:
#     def __repr__(self):
#         class_name = self.__class__.__name__
#         class_dict = self.__dict__
#         class_repr = f'{class_name}({class_dict})'
#         return class_repr
    

@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome
    
    def falar_nome(self):
         return f'O planeta é {self.nome}'


# Time = adiciona_repr(Time) # Ao invés disse coloca-se um decorador @adiciona_repr em cima das classes.
brasil = Time('Brasil')
portugal = Time('Portugal')

# Planeta = adiciona_repr(Planeta) # Ao invés disse coloca-se um decorador @adiciona_repr em cima das classes.
terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)
print(terra)
print(marte)

print(terra.falar_nome())
print(marte.falar_nome())