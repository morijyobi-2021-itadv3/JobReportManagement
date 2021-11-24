import hashlib
import string
import secrets

def sha256_text(text,salt):
   """与えられた文字列をSHA-256に変換する

   Args:
       text (string): パスワードの平文
       salt (string): ソルト

   Returns:
       string: 変換後の文字列(16進数)

   ソルトが存在しない場合、textのみでハッシュ値を生成する。
   
   """
   hash = hashlib.sha256(text+salt).hexdigest()

   return hash

def generate_hash(length):
   """ランダムで安全な文字列を暗号学的に作成する

   Args:
       length (Number): 生成する文字列の長さを指定

   Returns:
       string: 生成された安全な文字列
   """

   letters = string.ascii_letters
   result_str = ''.join(secrets.choice(letters) for i in range(length))
   return result_str





