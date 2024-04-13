"""
string.Template para substituir variáveis em textos 
doc: https://docs.python.org/3/library/string.html#template-strings 
Métodos: substitute: substitui mas gera erros se faltar chaves 
safe_substitute: substitui sem gerar erros Você também pode trocar o 
delimitador e outras coisas criando uma subclasse de template. 
"""
import json
import locale
import string
from datetime import datetime
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / 'aula183.txt'

locale.setlocale(locale.LC_ALL, '')


def converte_para_brl(numero: float) -> str:
    brl = 'R$ ' + locale.currency(val=numero, symbol=False, grouping=True)
    return brl


data = datetime(2022, 12, 28)
dados = dict(
    nome='Joao',
    valor=converte_para_brl(1_234_567),
    data=data.strftime('%d/%m/%Y'),
    empresa='O. M.',
    # telefone=' +55 (11) 7890-5432'
)

# print(dados)

print(json.dumps(dados, ident=2, ensure_ascii=False))

texto = '''
Prezado(a) $nome,

Informamos que sua mensalidade será cobrada no valor de ${valor} no dia $data.
Caso deseje cancelar o serviço, entre em contato com a $empresa pelo telefone $telefone.


Atenciosamente,
${empresa},
Abraços
'''

template = string.Template(texto)
# print(template.substitute(dados)) # Esse poderá apresentar erro caso falte argumento(s) para ser passado. Exemplo: Telefone
# print(template.safe_substitute(dados)) # Nesse caso não apresentará ERRO.

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    texto = arquivo.read()
    template = string.Template(texto)
    print(template.substitute(dados))
