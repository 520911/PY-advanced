import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailSend:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.GMAIL_SMTP = "smtp.gmail.com"
        self.GMAIL_IMAP = "imap.gmail.com"

    def mail_send(self, recipients, subject, message):
        mail = MIMEMultipart()
        mail['From'] = self.login
        mail['To'] = ', '.join(recipients)
        mail['Subject'] = subject
        mail.attach(MIMEText(message))
        send_mail = smtplib.SMTP(self.GMAIL_SMTP, 587)
        send_mail.ehlo()
        send_mail.starttls()
        send_mail.ehlo()
        send_mail.login(self.login, self.password)
        send_mail.sendmail(self.login, send_mail, mail.as_string())
        send_mail.quit()

    def mail_receive(self, mail_box='inbox', header=None):
        mail_receive = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        mail_receive.login(self.login, self.password)
        mail_receive.list()
        mail_receive.select(mail_box)
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail_receive.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail_receive.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail_receive.logout()
        return email_message


if __name__ == '__main__':
    gmail = EmailSend('some_mail@gmail.com', 'password')
    gmail.mail_send(['vasya@email.com', 'petya@email.com'], 'Subject', 'Message')
    gmail.mail_receive()
