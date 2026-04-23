from database.db_helper import get_connection

def get_all_khoa():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT ma_khoa, ten_khoa FROM Khoa")
    data = cur.fetchall()
    conn.close()
    return data


def insert_khoa(ma_khoa, ten_khoa):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO Khoa VALUES (?, ?)", (ma_khoa, ten_khoa))
    conn.commit()
    conn.close()