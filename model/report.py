import psycopg2

from model.db import get_connection

def select_all():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT reports.id,reports.company,tests.stage,departments.name,students.graduation_year,reports.prefecture from reports "
                        + "JOIN users ON users.id = reports.student_id "
                        + "JOIN students ON students.id = users.id "
                        + "JOIN departments ON departments.id = students.department_id "
                        + "JOIN tests ON tests.report_id = reports.id "
                        + "ORDER BY reports.id, tests.stage"
                        # + "LIMIT 7"
                    )

        rows = cur.fetchall()

        return rows

    except KeyError:
        print("環境変数の設定がされていません")
    except psycopg2.OperationalError:
        print("DBに接続できません")
    except Exception:
        print("エラーが発生しました。", Exception)
 