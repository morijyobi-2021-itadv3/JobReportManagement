import psycopg2

def select_sample():
    conn = psycopg2.connect(
        host = 'ec2-35-169-43-5.compute-1.amazonaws.com',
        port = 5432,
        user = 'wdmuoqzuwmqegh',
        database = 'd71g2m62taps2r',
        password = 'a936306ea8e5edc4548d17ba6654f16b5292b92bd018b345ba902434e3203149'
    )

    cur = conn.cursor()
    cur.execute('SELECT * FROM sample;')
    results = cur.fetchall()

    cur.close()
    conn.close()

    return results