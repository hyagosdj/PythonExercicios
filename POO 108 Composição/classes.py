"""
Em relação de composição uma classe depende da outra
"""

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado)) #Class Endereco utilizada ao chamar o método insere_endereco

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        print(f'{self.nome}, foi apagado com sucesso.')
    
class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
        
    def __del__(self):
        print(f'{self.cidade}/{self.estado}, foi apagado com sucesso.')