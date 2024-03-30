"""
https://rszalski.github.io/magicmethods/
"""

class A:
    def __init__(self):
        pass

    """ def __call__(self, *args, **kwargs):
        resultado = 1

        for i in args:
            resultado *= i
        return resultado """

    def __setattr__(self, __name: str, __value: any):
        self.__dict__[__name] = __value
        print(__name, __value)


a = A()
a.nome = 'Hyago Santos'
