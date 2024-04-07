# os.path.getsize e os.stat para dados dos arquivos
import math
import os
from itertools import count


def formata_tamanho(tamanho_em_bytes: int, base: int = 1024) -> str:
    """Formata um tamanh, de bytes para o tamanho apropriado"""

    # Original:
    # https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python

    # Se o tamanho for menor ou igual a 0, 0B.
    if tamanho_em_bytes <= 0:
        return "0B"
    # Tupla com os tamanhos
    #                      0     1     2     3     4     5
    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"
    # Logaritmo -> https://brasilescola.uol.com.br/matematica/logaritmo.htm
    # math.log vai retornar o logaritmo do tamanho_em_bytes
    # com a base (1024 por padrão), isso deve bater
    # com o nosso índice na abreviação dos tamanhos
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    # Por quanto nosso tamanho deve ser dividido para gerar o tamanho
    # correto.
    potencia = base ** indice_abreviacao_tamanhos
    # Nosso tamanho final
    tamanho_final = tamanho_em_bytes / potencia # round(tamanho_em_bytes / potencia, 2)
    # A abreviação que queremos
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final:.2f} {abreviacao_tamanho}' # Tamanho final :.2f caso não use o round()

# print(formata_tamanho(1_000))
# print(formata_tamanho(1_000_000))
# print(formata_tamanho(1_000_000_000))
# print(formata_tamanho(1_000_000_000_000))
# print(formata_tamanho(1_000_000_000_000_000))
# print(formata_tamanho(1_000_000_000_000_000_000)) # Pela base 1000 não localiza nesse caso usar base 1024

caminho = os.path.join('/Users', 'Hyago', 'Desktop', 'EXEMPLO')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print('  ', the_counter, 'Dir:', dir_)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        # tamanho = os.path.getsize(caminho_completo_arquivo) # Maneira simplificada
        stats = os.stat(caminho_completo_arquivo) # EXTENSA
        tamanho = stats.st_size # EXTENSA
        print('  ', the_counter, 'FILE:', file_, formata_tamanho(tamanho))
        # :warning:
        # Uma função de excluir de maneira permanente um determinado arquivo:
        # os.unlink(caminho dos arquivos que deseja excluir PEMANENTEMENTE).
