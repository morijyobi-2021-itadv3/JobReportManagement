import smtplib, ssl, os
from email.mime.text import MIMEText


def smtp_send_mail(to_email, message):
    """
  メール送信用メソッド
  Args:
    to_email(string): 送信先メールアドレス
    message: 本文
  Returns:
    なし
  """

    account = os.environ['SEND_MAIL_ADDRESS']
    password = os.environ['SMTP_PASSWORD']

    from_email = account

    message = MIMEText(message, 'html')
    message['Subject'] = '[No reply]ユーザー登録の通知'
    message['To'] = to_email
    message['From'] = from_email

    # サーバを指定する
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context())
    # 認証を行う
    server.login(account, password)
    # メールを送信する
    server.send_message(message)
    # 閉じる
    server.quit()
