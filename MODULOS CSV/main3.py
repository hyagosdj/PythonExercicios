import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula180.csv'

lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]  # Dicionario

with open(CAMINHO_CSV, 'w', encoding="utf-8") as arquivo:
    nome_colunas = lista_clientes[0].keys()  # Dicionário
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
    )

    escritor.writeheader()

    for cliente in lista_clientes:
        escritor.writerow(cliente)  # Dicionário
        # escritor.writerow(cliente.values())  # Dicionário

# Trabalhando com Lista
# lista_clientes = [
#     ['Luiz Otávio', 'Av 1, 22'],
#     ['João Silva', 'R. 2, "1"'],
#     ['Maria Sol', 'Av B, 3A'],
# ]

# with open(CAMINHO_CSV, 'w', encoding="utf-8") as arquivo:
#     nome_colunas = ['Nome', 'Endereço']  # Lista
#     escritor = csv.writer(arquivo)

#     escritor.writerow(nome_colunas)

#     for cliente in lista_clientes:
#         escritor.writerow(cliente)  # Lista
