import smtplib
from email.mime.text import MIMEText

SENDER_EMAIL = "mandritadasgupta03@gmail.com"
APP_PASSWORD = "mandrita2004@"

RECEIVER_EMAIL = "mandritadasgupta16@gmail.com"

def send_fire_alert(confidence):

    subject = "🔥 FIRE & SMOKE DETECTED - IOCL Monitoring System"

    body = f"""
Fire Detected

Confidence: {confidence}

Immediate attention required.
"""

    msg = MIMEText(body)

    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    try:

        server = smtplib.SMTP("smtp.gmail.com",587)

        server.starttls()

        server.login(
            SENDER_EMAIL,
            APP_PASSWORD
        )

        server.sendmail(
            SENDER_EMAIL,
            RECEIVER_EMAIL,
            msg.as_string()
        )

        server.quit()

        print("Email Sent")

    except Exception as e:

        print(e)