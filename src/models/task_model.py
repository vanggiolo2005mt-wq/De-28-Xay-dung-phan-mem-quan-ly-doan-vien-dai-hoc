from database.db_helper import get_connection

def get_all_task():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM Task")
    data = cur.fetchall()

    conn.close()
    return data


def insert_task(ten_task, mo_ta, muc_do):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO Task(ten_task, mo_ta, muc_do)
        VALUES (?, ?, ?)
    """, (ten_task, mo_ta, muc_do))

    conn.commit()
    conn.close()