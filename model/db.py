import psycopg2

def select_sample():
    conn = psycopg2.connect(
        host = '172.21.0.2',
        port = 5432,
        user = 'admin',
        database = 'admin',
        password = 'example'
    )

    cur = conn.cursor()
    cur.execute('SELECT * FROM data;')
    results = cur.fetchall()

    cur.close()
    conn.close()

    return results