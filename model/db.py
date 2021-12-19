import psycopg2
import urllib.parse
import os


def get_connection():
    """DBのコネクションを返すメソッド
    Returns:
        成功時:Connection
        失敗時:None
    
    環境変数(DATABASE_URL)を使用します。

    環境変数の構成:
        "postgresql://{ホスト名}:{ポート番号}/{DB名}?user={ユーザ名}&password={パスワード}"

    """
    try:
        url = urllib.parse.urlparse(os.environ["DATABASE_URL"])
        conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )
        return conn
    except KeyError:
        print("環境変数の設定がされていません")
    except psycopg2.OperationalError:
        print("DBに接続できません")
    except Exception:
        print("エラーが発生しました。")
 