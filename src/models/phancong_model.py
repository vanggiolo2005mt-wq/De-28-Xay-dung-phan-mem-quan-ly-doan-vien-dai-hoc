from database.db_helper import get_connection

def get_phancong():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT pc.id, dv.ho_ten, hd.ten_hd, t.ten_task, pc.trang_thai
        FROM PhanCong pc
        JOIN DoanVien dv ON pc.ma_dv = dv.ma_dv
        JOIN HoatDong hd ON pc.ma_hd = hd.ma_hd
        JOIN Task t ON pc.ma_task = t.ma_task
    """)

    data = cur.fetchall()
    conn.close()
    return data