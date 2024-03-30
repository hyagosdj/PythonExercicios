from bancodedados import BaseDeDados

bd = BaseDeDados()
bd.inserir_cliente(1, 'Hyago')
bd.inserir_cliente(1, 'Hyago')
bd.inserir_cliente(2, 'Carlos')
bd.inserir_cliente(3, 'Virginia')

# Como a variável está protegida por __ e pelo Getter, o BD.DADOS apresentará um erro de AttributeError
bd.__dados = 'Uma outra coisa'
print(bd.dados)
bd.lista_clientes()

#print(bd.dados)