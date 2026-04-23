from database.db_helper import get_connection


def get_all_doanvien():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            dv.ma_dv,
            dv.ho_ten,
            dv.ngay_sinh,
            cd.ten_lop,
            k.ten_khoa,
            dv.ngay_vao_doan,
            dv.trang_thai
        FROM DoanVien dv
        JOIN ChiDoan cd ON dv.ma_lop = cd.ma_lop
        JOIN Khoa k ON cd.ma_khoa = k.ma_khoa
    """)

    data = cursor.fetchall()
    conn.close()
    return data