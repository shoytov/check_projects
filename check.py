import requests
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
import smtplib


def check() -> None:
    """ проходит по списку проектов в файле и записывает недоступные проекты в лог-файл """

    errors = False
    with open('projects.txt', 'r') as fp:
        with open('log.txt', 'w') as log:
            for line in fp:
                try:
                    response = requests.get(line)
                    
                    if response.status_code != 200:
                        log.write(line)
                        log.write(str(response.status_code))
                        errors = True
                except Exception as e:
                    log.write(line)
                    log.write(str(e))
                    errors = True
    
    # отправка письма в случае найденных недоступных сайтов
    if errors:
        msg = MIMEMultipart()
        message = "Есть недоступные проекты из вашего списка"
        
        password = os.environ['EMAIL_HOST_PASSWORD']
        msg['From'] = os.environ['DEFAULT_FROM_EMAIL']
        msg['To'] = os.environ['DEFAULT_TO_EMAIL']
        msg['Subject'] = "Недостпуные проекты"

        msg.attach(MIMEText(message, 'plain'))
        p = MIMEBase('application', 'octet-stream')

        filename = 'log.txt'
        with open(filename, 'rb') as fp:
            p.set_payload(fp.read())
        
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)

        server = smtplib.SMTP(os.environ['EMAIL_HOST'], os.environ['EMAIL_PORT'])
        server.starttls()
        server.login(msg['From'], password)

        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()


if __name__ == '__main__':
    check()
