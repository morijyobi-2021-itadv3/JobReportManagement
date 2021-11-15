import psycopg2

def select_sample():
    conn = psycopg2.connect(
        host = '',
        port = 5432,
        user = '',
        database = '',
        password = ''
    )

    cur = conn.cursor()
    cur.execute('SELECT * FROM sample;')
    results = cur.fetchall()

    cur.close()
    conn.close()

    return results