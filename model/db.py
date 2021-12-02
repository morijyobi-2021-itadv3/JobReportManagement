import psycopg2

def select_sample():
    conn = psycopg2.connect(
        host = 'db',
        port = 5432,
        user = 'jrm_tora',
        database = 'sample',
        password = 'jrm_tora_pass'
    )

    cur = conn.cursor()
    cur.execute('SELECT name,greet FROM users;')
    results = cur.fetchall()

    cur.close()
    conn.close()

    return results
