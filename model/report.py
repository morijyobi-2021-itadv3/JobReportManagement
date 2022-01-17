import psycopg2
import urllib.parse
import os

from model.db import get_connection

def select_all():
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
 