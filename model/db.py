import psycopg2
import os

def select_sample():
    conn = psycopg2.connect(
        host = os.environ.get('PSQL_DB_DOCKER_HOST'),
        port = os.environ.get('PSQL_DB_DOCKER_PORT'),
        user = os.environ.get('PSQL_DB_DOCKER_USER'),
        database = os.environ.get('PSQL_DB_DOCKER_DATABASE'),
        password = os.environ.get('PSQL_DB_DOCKER_PASSWORD')
    )

    cur = conn.cursor()
    cur.execute('SELECT * FROM data;')
    results = cur.fetchall()

    cur.close()
    conn.close()

    return results
