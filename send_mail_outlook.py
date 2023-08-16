
# coding: UTF-8

# send_mail_outlook.py

import win32com.client as win32

def send_email(subject, body, recipients):

    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)

    mail.Subject = subject
    mail.HTMLBody = f"""<html><body>{body}<br><br>{get_signature()}</body></html>"""
    mail.To = ';'.join(recipients)

    mail.Send()

def get_signature():

    img_src = r"signature.png"
    signature = f"""
    <img src="{img_src}" alt="Assinatura">
    """
    return signature

subject = 'Assunto'
body = 'E-mail enviado com sucesso!'
recipients = ['outlook@hotmail.com']

send_email(subject, body, recipients)
