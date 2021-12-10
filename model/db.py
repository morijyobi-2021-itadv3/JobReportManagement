import psycopg2
from dotenv import load_dotenv
import os

load_dotenv(override=True)

def select_sample():
    conn = psycopg2.connect(
        host = '',
        port = '',
        user = os.getenv('PG_USER'),
        database = os.getenv('PG_DATABASE'),
        password = ''
    )

    cur = conn.cursor()
    cur.execute('SELECT * FROM departments;')
    results = cur.fetchall()

    cur.close()
    conn.close()

    return results
