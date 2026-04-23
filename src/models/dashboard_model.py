from database.db_helper import get_connection


# =============================
# THỐNG KÊ
# =============================
def get_stats():
    conn = get_connection()
    cursor = conn.cursor()

    # tổng đoàn viên
    cursor.execute("SELECT COUNT(*) FROM DoanVien")
    tong = cursor.fetchone()[0]

    # đang hoạt động
    cursor.execute("SELECT COUNT(*) FROM DoanVien WHERE trang_thai = 'Hoạt động'")
    dang_hd = cursor.fetchone()[0]

    # chưa đóng đoàn phí (ví dụ tháng 1/2026)
    cursor.execute("""
    SELECT COUNT(*) 
    FROM DoanVien dv
    LEFT JOIN DoanPhi dp 
        ON dv.ma_dv = dp.ma_dv AND dp.thang = 1 AND dp.nam = 2026
    WHERE dp.trang_thai IS NULL OR dp.trang_thai = 'Chưa đóng'
    """)
    chua_dong = cursor.fetchone()[0]

    # tỷ lệ
    ty_le = int((dang_hd / tong) * 100) if tong > 0 else 0

    conn.close()

    return {
        "tong": tong,
        "dang_hd": dang_hd,
        "chua_dong": chua_dong,
        "ty_le": f"{ty_le}%"
    }


# =============================
# HOẠT ĐỘNG GẦN ĐÂY
# =============================
def get_recent_activities():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT ma_hd, ten_hd, ngay, dia_diem
    FROM HoatDong
    ORDER BY ngay DESC
    LIMIT 5
    """)

    data = cursor.fetchall()
    conn.close()

    return data