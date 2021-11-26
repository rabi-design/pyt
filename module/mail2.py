import smtplib, ssl
from email.mime.text import MIMEText


def mail(from_ad, to_ad, password, subject, message):
    # 送受信先
    # to_email = "snowsnow123@ezweb.ne.jp"
    # from_email = "g2181017@tcu.ac.jp"

    smtp_host = 'smtp.tcu.ac.jp'
    smtp_port = 465
    username = from_ad # "g2181017@tcu.ac.jp"
    # password = 'Yuki1311'
    # サーバを指定する
    # message = "メール本文"
    msg = MIMEText(message, "html")
    msg["Subject"] = subject
    msg["To"] = to_ad
    msg["From"] = from_ad
    server = smtplib.SMTP_SSL(smtp_host, smtp_port, context=ssl.create_default_context())
    server.login(username, password)

    # メールを送信する
    server.send_message(msg)
    # 閉じる
    server.quit()


if __name__ == "__main__":
    mail()
