# -*- coding: utf-8 -*-
import smtplib
from random import shuffle
print('~'*30)
print('»» Sorteador de Anjo ««')
print('~'*30)

n=int(input('Digite o numero de pessoas participantes: '))

while n%2==1:
    print('O numero de participantes tem que ser par!')
    n=int(input('Digite o numero de pessoas participantes: '))

informacoes = []

for i in range (0, n):
    nome = str(input('\nDigite o nome de um componente:')).strip()
    email = str(input('Digite o email de {}: '.format(nome))).strip()
    informacoes.append(nome + ' ' + email)

shuffle(informacoes)

for i in range(-1, n-1):
    if i == -1:
        protegido = informacoes[n-1].split()
        destinatario = informacoes[0].split()
    else:
        protegido = informacoes[i].split()
        destinatario = informacoes[i+1].split()


    # Credenciais
    remetente = 'anjoencontraoneves@gmail.com' #https://myaccount.google.com/lesssecureapps?hl=pt-BR << Dar autorização a apps menos seguros
    senha = 'encontrao2018'

    # Informações da mensagem
    destinatario = destinatario[1]
    assunto = 'Seu Protegido: '
    texto = protegido[0]

    # Preparando a mensagem
    msg = '\r\n'.join([
        'From: %s' % remetente,
        'To: %s' % destinatario,
        'Subject: %s' % assunto,
        '',
        '%s' % texto
    ])

    # Enviando o email
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(remetente, senha)
    server.sendmail(remetente, destinatario, msg)
    server.quit()
    print ('{} Emails Enviados'.format(i+2))
