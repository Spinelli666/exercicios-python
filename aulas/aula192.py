# + Web Scraping com Python usando requests e bs4 BeautifulSoup
# - Web Scraping é o ato de "raspar a web" buscando informações de forma
# automatizada, com determinada linguagem de programação, para uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# + Instalação
# - pip install requests types-requests bs4

import re

import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')

# if parsed_html.title is not None:
#     print(parsed_html.title.text)

headings = parsed_html.select_one('div.small-widget:nth-child(1) > h2:nth-child(1)')

if headings is not None:
    article = headings.parent
    
    if article is not None:
        for p in article.select('p'):
            # print(p.text)
            print(re.sub(r'\s{1,}', ' ', p.text).strip())