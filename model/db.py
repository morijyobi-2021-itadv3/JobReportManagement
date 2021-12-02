import psycopg2

def select_sample():
    conn = psycopg2.connect(
        host = 'db',
        port = 5432,
        user = 'admin',
        database = 'admin',
        password = 'example'
    )

    cur = conn.cursor()
    cur.execute('SELECT * FROM users;')
    results = cur.fetchall()

    cur.close()
    conn.close()

    return results
