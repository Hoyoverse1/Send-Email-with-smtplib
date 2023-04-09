import smtplib

sender_email = 'example@gmail.com'
sender_password = 'password'

receiver_email = 'recipient@example.com'

subject = 'Contoh Email'
body = 'Ini adalah contoh email yang dikirim menggunakan Python.'

smtp_server = 'smtp.gmail.com'
smtp_port = 587

server = smtplib.SMTP(smtp_server, smtp_port)

server.starttls()
server.login(sender_email, sender_password)

message = f'Subject: {subject}\n\n{body}'

server.sendmail(sender_email, receiver_email, message)

server.quit()
