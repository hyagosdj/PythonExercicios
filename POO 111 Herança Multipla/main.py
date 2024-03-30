class A:
    def falar(self):
        print('Falando.. Estou em A.')

    
class B(A):
    def falar(self):
        print('Falando.. Estou em B.')


class C(A):
    def falar(self):
        print('Falando.. Estou em C.')


class D(B, C):
    pass

d = D()
d.falar()

""" from smartphone import Smartphone

smartphone = Smartphone('Pocophone F1')
smartphone.conectar()
smartphone.desligar()
smartphone.ligar()
smartphone.conectar()
smartphone.conectar()
smartphone.conectar()
smartphone.desligar()
smartphone.conectar()
smartphone.desligar()
smartphone.desconectar()
 """