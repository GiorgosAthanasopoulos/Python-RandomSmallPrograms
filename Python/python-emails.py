import smtplib, ssl

server = smtplib.SMTP(host='smtp-mail.outlook.com',port=587)
server.ehlo()
server.starttls()
server.login(input('enter account email'),input('enter account password'))
subject = input('enter subject')
body = input('enter email body')
message = f'Subject: {subject}\n\n{body}'
server.sendmail(input('enter account email again'), input('enter recipient email'), message)
server.quit()
