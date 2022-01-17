import psycopg2
import urllib.parse
import os

from model.db import get_connection

def select_all():
    """DBのコネクションを返すメソッド
    Args:
        なし
    Returns:
        成功時:Connection
        失敗時:None
    
    環境変数(DATABASE_URL)を使用します。

    環境変数の構成:
        "postgresql://{ホスト名}:{ポート番号}/{DB名}?user={ユーザ名}&password={パスワード}"

    """
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * from reports")

        rows = cur.fetchall()

        return rows

    except KeyError:
        print("環境変数の設定がされていません")
    except psycopg2.OperationalError:
        print("DBに接続できません")
    except Exception:
        print("エラーが発生しました。")
 