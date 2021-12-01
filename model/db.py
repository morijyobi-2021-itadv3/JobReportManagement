import psycopg2
import os

def select_sample():
    conn = psycopg2.connect(
        host = os.environ.get('POSTGRES_HOST'),
        port = os.environ.get('POSTGRES_PORT'),
        user = os.environ.get('POSTGRES_USER'),
        database = os.environ.get('POSTGRES_DB'),
        password = os.environ.get('POSTGRES_PASSWORD')
    )

    cur = conn.cursor()
    cur.execute('SELECT * FROM sample;')
    results = cur.fetchall()

    cur.close()
    conn.close()

    return results
