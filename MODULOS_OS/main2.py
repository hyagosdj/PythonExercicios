# os.listdir para navegar em caminhos
# C:/Users/Hyago/Desktop/EXEMPLO
# caminho = r'C:\\Users\\Hyago\\Desktop\\EXEMPLO'
# import os

# caminho = os.path.join('/Users', 'Hyago', 'Desktop', 'EXEMPLO')
# print(caminho)

# for pasta in os.listdir(caminho):
#     caminho_completo_pasta = os.path.join(caminho, pasta)
#     print(caminho_completo_pasta)
#     print(pasta)
#     if not os.path.isdir(caminho_completo_pasta):
#         continue

#     for imagem in os.listdir(caminho_completo_pasta):
#         print('  ', imagem)


"""
os.walk
os.walk é uma função que permite percorrer uma estrutura de diretórios de
maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
e uma lista dos arquivos do diretório atual (files).
"""
import os
from itertools import count

caminho = os.path.join('/Users', 'Hyago', 'Desktop', 'EXEMPLO')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print('  ', the_counter, 'Dir:', dir_)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        print('  ', the_counter, 'FILE:', file_)
        
# :warning:
# Uma função de excluir de maneira permanente um determinado arquivo:
# os.unlink(caminho dos arquivos que deseja excluir PEMANENTEMENTE).
