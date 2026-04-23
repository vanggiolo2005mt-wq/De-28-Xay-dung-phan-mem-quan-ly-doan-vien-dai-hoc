from database.db_helper import get_connection

def get_diemdanh(ma_hd):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT dv.ho_ten, dd.co_mat, dd.ghi_chu
        FROM DiemDanh dd
        JOIN DoanVien dv ON dd.ma_dv = dv.ma_dv
        WHERE dd.ma_hd = ?
    """, (ma_hd,))

    data = cur.fetchall()
    conn.close()
    return data