import psycopg2
import os


def select_sample():
    conn = psycopg2.connect(
        host = os.environ.get('POSTGRES_HOST'),
        port = os.environ.get('POSTGRES_PORT'),
        user = os.environ.get('POSTGRES_USER'),
        database = os.environ.get('POSTGRES_DATABASE'),
        password = os.environ.get('POSTGRES_PASSWORD')
    )

    cur = conn.cursor()
    cur.execute('SELECT name,greet FROM users;')
    results = cur.fetchall()

    cur.close()
    conn.close()

    return results
