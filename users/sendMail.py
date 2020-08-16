
import smtplib ,ssl 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# MAIL_DRIVER=smtp
# MAIL_HOST=ssl://smtp.gmail.com
# MAIL_PORT=465
# MAIL_USERNAME=ahomtechnology@gmail.com
# MAIL_PASSWORD='ahom@123'
# MAIL_ENCRYPTION=null

def send_mail_digest(receiver, receiverName, subject, password):

    msg = MIMEMultipart()
    msg['From'] = "MriCheck < ahomtechnology@gmail.com >"
    msg['To'] = receiverName +" < " +receiver +">"
    msg['Subject'] = subject
    message_cont2= """
<html>

<head></head>

<body>
    <div style="width: 100%; padding: 24px 10px 15px 10px;background-color: #f5f5f5;">
        <p>Welcome {content_task1},</p>

        <p>
            Thanks for Registration. <br/> This is an automated email to notify you that your Registration is successful.
        </p>

        <p>
        Thanks,<br/>
        MriCheck Team.
        </p>
    </div>
</body>

</html>""".format(content_task1=receiverName, content_subj1=password)

    msg.attach(MIMEText(message_cont2, 'html'))

    try:
        smtp_server ='smtp.gmail.com'
        sender_email ='ahomtechnology@gmail.com'
        password ='ahom@123'
        port = '587'
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver, msg.as_string)
            server.quit()

        # server = smtplib.SMTP(rec, rec3)
        # # server.connect("smtp.taazzabasket.com",587)
        # server.ehlo()
        # server.starttls()
        # server.login(rec1, rec2)
        # server.sendmail( msg['From'], receiver, msg.as_string())
        # server.close()
        return 1
    except Exception as e:
        print('Unable to send mail : '+ str(e))
        return 0