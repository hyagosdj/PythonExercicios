"""
EM PYTHON TUDO É UM OBJETO: incluindo classes
Metaclasses são as "classes" que criam classes.
type é uma metaclasse (!!!???)

### type serve para criar CLASSES ###
"""
# CLASSE
""" class A:
    attr = 'Valor'


# INSTANCIAS DA CLASSE (OBJETOS CRIADOS PELA CLASS A)
a = A()
b = A()
c = A() """

"""class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)
        #print(namespace)

        if 'b_fala' not in namespace:
            print(f'Oi, você precisa criar o método b_fala em {name}')
        else:
            if not callable(namespace['b_fala']):
                print(f'b_fala precisa ser um método, não atributo em {name}.')
        if 'attr_classe' in namespace:
            print(f'{name} tentou sobrescrever o atribulo.')
            del namespace['attr_classe']

        if name == 'B':
            return type.__new__(mcs, name, bases, namespace)
        print(namespace)
        
        return type.__new__(mcs, name, bases, namespace)

class A(metaclass=Meta):
    attr_classe = 'Valor A'
    def fala(self):
        self.b_fala()
    
    class B(A):
        attr_classe = 'Valor B'
        teste = 'Valor'

    def b_fala(self):
        print('Oi')
    def sei_la(self):
        pass
class C(B):
    attr_classe = 'Valor C'

c = C()
print(c.attr_classe) """

A = type(
    'A',
    (),
    {
        'attr': 'Olá Mundo!'
    }
)

a = A()
print(a.attr)