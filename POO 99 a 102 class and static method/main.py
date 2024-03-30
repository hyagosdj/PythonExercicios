from pessoa import Pessoa

p1 = Pessoa('Luiz', 23)
p2 = Pessoa('Maria', 18)

p1.comer('Laranja')
p1.parar_comer()
p1.falar('POO')
p1.falar('POO')
p1.parar_comer()
p1.comer('Maça')
p1.parar_falar()
p1.comer('Maçã')
p1.get_ano_nascimento()
p2.get_ano_nascimento()
print(Pessoa.gera_id())
print(p1.gera_id())
print(p1.nome, p1.idade)