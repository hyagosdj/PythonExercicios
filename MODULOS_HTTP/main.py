#  O módulo requests para requisições HTTP no python
# HTTP (HyperText Transfer Protocol) é um protocolo usado enviar e receber
# dados na Internet. Ele funciona no modo cliente/servidor, onde o cliente
# (seu navegador, por exemplo) faz uma requisição ao servidor
# (site, por exemplo), que responde com os dados adequados.
#
# A mensagem de requisição do cliente deve incluir dados como:
# - O método HTTP
#       - Leitura (safe) - GET, HEAD (cabeçalhos), OPTIONS (métodos suportados)
#       - Escrita - POST, PUT (substitui), PATH (atualiza), DELETE
# - O endereço do recurso a ser acessado (/users/)
# - Os cabeçalhos HTTP (Content-Type, Authorization)
# - O Corpo da mensagem (caso necessário, de acordo com o método HTTP)
#
# A mensagem de resposta do servidor deve incluir dados como:
# - código de status HTTP (200 success, 404 Not found, 301 Moved Permanently)
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
# - Os cabeçalhos HTTP (Content-Type, Accept)
# - O corpo da mensagem (Pode estar em vazio em alguns casos)

# CRIE UM DIRETORIO cole o código do site disponivel na aula 310: aula190_site
# para obter informações no site para usarmos na aula

# ATIVE SEU AMBIENTE VIRTUAL, UTILIZE:
# python -m http.server -d aula190_site/ 3333
# Selecione uma porta aleatória/generica

# pip install requests types-requests

# requests para requisições HTTP
# Tutorial -> https://youtu.be/Qd8JT0bnJGs
# import requests (dará erro caso não possua módulo requests)
import requests

# http:// -> 80 | https:// -> 443
url = 'http://localhost:3333/'
# Se o seu terminal tiver opção para duas abas, abra-as,
# caso contrario abra 2x
# Suba o servidor criado em um dos tais.
response = requests.get(url)

print(response.status_code)
# print(response.headers)
# print(response.content)
# print(response.json())
print(response.text)
