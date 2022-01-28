import smtplib,ssl,os
from email.mime.text import MIMEText

def  send_mail(to_email,user_password):
  """
  新しく追加されたユーザーのメールアドレスに仮パスワードを送信する

  Args:
    to_email(string): 送信先メールアドレス
    user_password(string): 自動生成された仮パスワード
  Returns:
    なし
  """
  # SMTP認証情報
  account = 'jobreportmanagementsystem@gmail.com'
  password = os.environ['SMTP_PASSWORD']

  # 送受信先
  from_email = 'jobreportmanagementsystem@gmail.com'

  # MIMETextを作成
  message = '''
  <p>管理者により「<strong>就活報告書管理システム</strong>」のユーザー登録が完了しました。</p>
  <p>本システムを利用する場合は下記ログイン情報を使用してください。</p>
  <hr>
  <p><strong>ログイン情報</strong></p>
  <div>メールアドレス：{0}</div>
  <div>仮パスワード：{1}</div>
  '''.format(to_email,user_password)

  msg = MIMEText(message, 'html')
  msg['Subject'] = '[No reply]ユーザー登録の通知'
  msg['To'] = to_email
  msg['From'] = from_email

  # サーバを指定する
  server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context())
  # 認証を行う
  server.login(account, password)
  # メールを送信する
  server.send_message(msg)
  # 閉じる
  server.quit()
