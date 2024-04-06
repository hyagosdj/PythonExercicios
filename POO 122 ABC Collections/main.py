"""
Implementando o protocolo do Iterator em Python
Essa é apenas uma aula para introduzir os protocolos de collections.abc no
Python. Qualquer outro protocolo poderá ser implementando seguindo a mesma
estrutura dessa aula.

https://docs.python.org/3/library/collections.abc.html
"""

# from collections.abc import Iterable, Iterator
from collections.abc import Sequence


class MyList(Sequence):
    def __init__(self) -> None:
        self._data = {}
        self._index = 0
        self._next_index = 0

    def append(self, *values):
        for value in values:
            self._data[self._index] = value
            self._index += 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration


        value = self._data[self._next_index]
        self._next_index += 1
        return value

    def __len__(self) -> int:
        return self._index

    def __getitem__(self, index):
        print('getitem', index)
        return self._data[index]
    
    def __setitem__(self, index, value):
        print('setitem', index)
        self._data[index] = value


if __name__ == '__main__':
    lista = MyList()
    lista[0] = 'Joao'
    lista.append('Maria', 'Helena')
    lista.append('Luiz')
    # print(lista._data)
    # print(lista[0])
    # print(len(lista))
    for item in lista:
        print(item)
    print('---')

    for item in lista:
        print(item)
    print('---')
