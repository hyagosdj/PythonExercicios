from classes import *

"""
Associação - USA | Agregação - TEM | Composição - É DONO | Herança - É
"""

c1 = Cliente('Hyago', 26)
print(f'O(A) {c1.nome} tem {c1.idade} anos')
c1.falar()
c1.comprar()

print()

a1 = Aluno('Joaquina', 86)
print(f'O(A) {a1.nome} tem {a1.idade} anos')
a1.falar()
a1.estudar()

print()

p1 = Pessoa('João', 30) # Não possui os métodos específicos das anteriores.
print(f'O(A) {p1.nome} tem {p1.idade} anos')
p1.falar()
