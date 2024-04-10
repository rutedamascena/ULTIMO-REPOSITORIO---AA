
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
from scraping import dados_html
from dotenv import load_dotenv 
import os


def enviar_email_com_html(html):
    smtp_server = "smtp-relay.brevo.com"
    port = 587
    email = "damascenarute@gmail.com"
    password = os.getenv ('CHAVE_EMAIL')
    remetente = "damascenarute@gmail.com"
    destinatario_email = "anadirdamascena@gmail.com"

    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario_email
    msg['Subject'] = 'E-mail com Dados do Clipping'

    msg.attach(MIMEText(html, 'html'))

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(email, password)
        server.sendmail(remetente, msg['To'], msg.as_string())

enviar_email_com_html(dados_html)