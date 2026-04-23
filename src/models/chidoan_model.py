from database.db_helper import get_connection


def get_all_chidoan():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT ma_lop, ten_lop
        FROM ChiDoan
    """)

    return cur.fetchall()
# lọc theo khoa
def get_chidoan_by_khoa(ma_khoa):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT ma_lop, ten_lop
        FROM ChiDoan
        WHERE ma_khoa = ?
        ORDER BY ten_lop
    """, (ma_khoa,))

    data = cursor.fetchall()
    conn.close()
    return data

# láy ds khoa
def get_all_khoa():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT ma_khoa, ten_khoa
        FROM Khoa
        ORDER BY ten_khoa
    """)

    data = cursor.fetchall()
    conn.close()
    return data

