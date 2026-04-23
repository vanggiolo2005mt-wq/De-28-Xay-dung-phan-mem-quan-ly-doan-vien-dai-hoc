from database.db_helper import get_connection


# =========================
# LẤY HOẠT ĐỘNG
# =========================
def get_all_hoatdong():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT ma_hd, ten_hd, ngay, dia_diem, noi_dung
        FROM HoatDong
        ORDER BY ngay DESC
    """)

    data = cursor.fetchall()
    conn.close()
    return data


# =========================
# THÊM HOẠT ĐỘNG
# =========================
def insert_hoatdong(ma, ten, ngay, diadiem, noidung):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO HoatDong
        (ma_hd, ten_hd, ngay, dia_diem, noi_dung)
        VALUES (?, ?, ?, ?, ?)
    """, (ma, ten, ngay, diadiem, noidung))

    conn.commit()
    conn.close()

# =========================
def update_hoatdong(ma, ten, ngay, diadiem, noidung):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE HoatDong
        SET ten_hd=?, ngay=?, dia_diem=?, noi_dung=?
        WHERE ma_hd=?
    """, (ten, ngay, diadiem, noidung, ma))

    conn.commit()
    conn.close()

# XÓA
def delete_hoatdong(ma):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM HoatDong
        WHERE ma_hd = ?
    """, (ma,))

    conn.commit()
    conn.close()