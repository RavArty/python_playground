import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Rav Art'
email['to'] = 'ravkart@gmail.com'
email['subject'] = 'test email from py'

email.set_content('I am here')

with smtplib.SMTP(host='smtp.mail.yahoo.com', port=465) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('your_email', 'your_pass')
	smtp.send_message(email)
	print('done')