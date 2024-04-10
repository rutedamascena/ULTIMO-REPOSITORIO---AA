from flask import Flask, render_template, url_for, request
from scraping import dados_html 
from envio_email import enviar_email_com_html

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/sobremim')
def sobre_mim():
    return render_template('sobremim.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/dinamica')
def dinamica():
    return render_template('dinamica.html',dados_html=dados_html)

@app.route('/processar_busca', methods=['POST'])
def processar_busca():
    url = 'https://www.bahianoticias.com.br/pesquisa/petrobras'
    return render_template('dinamica.html', dados_html=dados_html)


@app.route('/destinatarios', methods=['POST'])
def enviar_email():
    destinatario_email = request.form['destinatario_email']
    enviar_email_com_html(dados_html)
    return render_template('dinamica.html', destinatario_email,dados_html=dados_html)