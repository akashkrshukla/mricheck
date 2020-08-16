
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail_digest(receiver, receiverName, subject, password):

    msg = MIMEMultipart()
    msg['From'] = "Skyline Golf < info.skylinegolf@gmail.com >"
    msg['To'] = receiverName +" < " +receiver +">"
    msg['Subject'] = subject
    message_cont2= """
<html>

<head></head>

<body>
    <div style="width: 100%; padding: 24px 10px 15px 10px;background-color: #f5f5f5;">
        <p>Welcome {content_task1},</p>

        <p>
            Thanks for Registration. <br/> This is an automated email to notify you that your password for Skyline is: {content_subj1}
        </p>

        <p>
        Thanks,<br/>
        Skyline Team.
        </p>
    </div>
</body>

</html>""".format(content_task1=receiverName, content_subj1=password)

    msg.attach(MIMEText(message_cont2, 'html'))

    try:
        rec ='smtp.gmail.com'
        rec1 ='info.skylinegolf@gmail.com'
        rec2 ='sky@7890'
        rec3 = '587'
        server = smtplib.SMTP(rec, rec3)
        # server.connect("smtp.taazzabasket.com",587)
        server.ehlo()
        server.starttls()
        server.login(rec1, rec2)
        server.sendmail( msg['From'], receiver, msg.as_string())
        server.close()
        return 1
    except Exception as e:
        print('Unable to send mail : '+ str(e))
        return 0