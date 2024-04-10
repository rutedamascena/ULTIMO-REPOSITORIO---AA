import requests
import bs4
import pandas as pd

def gerar_dados_html(url):
    requisicao = requests.get(url)
    if requisicao.status_code == 200:
        html = requisicao.content
        sopa = bs4.BeautifulSoup(html, 'html.parser')
        clipping_bahianoticias = sopa.findAll('div', {'class': 'sc-3c754a49-0 edpZTL'})
        titulos = []
        links = []
        for noticia in clipping_bahianoticias:
            titulo = noticia.find('h3', {'class': 'sc-3c754a49-2 iihoil'}).text.strip()
            link = 'https://www.bahianoticias.com.br' + noticia.find('a').get('href')
            titulos.append(titulo)
            links.append(link)
        dados_noticias = pd.DataFrame({'Título': titulos, 'Link': links})
        dados_noticias['Veículo'] = 'Bahia Notícias'
        html_formatado = dados_noticias.to_html(index=False)
        return html_formatado
    else:
        return None

url = 'https://www.bahianoticias.com.br/pesquisa/petrobras'
dados_html = gerar_dados_html(url)
print(dados_html)