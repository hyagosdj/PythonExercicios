# - Web Scraping com Python usando requests e bs4 BeatifulSoup
# - Web Scraping é o ato de "raspar a web" buscando informações de form
# automatizada, com determinada linguagemde programação, para uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeatifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - Doc: https://www.crummy.com/software/BeatifulSoup/bs4/doc.ptbr/
# - Instalação
# - pip install requests types-requests bs4

# Expressão regular para retirar os espaços que estão no retorno de p
import re

import requests
from bs4 import BeautifulSoup  # type: ignore

url = 'http://127.0.0.1:3333/'
response = requests.get(url)
bytes_html = response.content
# raw_html = response.text
parsed_html = BeautifulSoup(bytes_html, 'html.parser', from_encoding='utf-8')

# print(parsed_html)
# print(parsed_html.title.text) # Esse erro é devido ao método title retornar
# duas coisas. tag | None
# Para solucionar o problema deve ser feito a verificação:
# if parsed_html.title.text is not None:
#     print(parsed_html.title.text)

top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2')
if top_jobs_heading.text is not None:  # type: ignore
    # print(top_jobs_heading.text)  # type: ignore
    article = top_jobs_heading.parent  # type: ignore
    print(article)

    # Para pegar todos os paragrafos deste ARTICLE
    if article is not None:
        for p in article.select('p'):
            print(re.sub(r'\s{1,}', ' ', p.text).strip())
