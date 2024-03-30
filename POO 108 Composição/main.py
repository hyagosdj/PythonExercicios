from classes import Cliente, Endereco

cliente1 = Cliente('Hyago', 26)
cliente1.insere_endereco('Fortaleza', 'CE')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()

cliente2 = Cliente('Samira', 33)
cliente2.insere_endereco('São Paulo', 'SP')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2.enderecos
print()

cliente3 = Cliente('João', 19)
cliente3.insere_endereco('Curitiba', 'SP')
print(cliente3.nome)
cliente3.lista_enderecos()
del cliente3
print()

print('*' * 60)