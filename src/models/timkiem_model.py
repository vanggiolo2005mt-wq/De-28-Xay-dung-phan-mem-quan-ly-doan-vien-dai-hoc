from database.db_helper import get_connection


# ==============================
# SEARCH ĐOÀN VIÊN
# ==============================
def search_doanvien(keyword):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
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
        WHERE 
            dv.ma_dv LIKE ?
            OR dv.ho_ten LIKE ?
            OR cd.ten_lop LIKE ?
            OR k.ten_khoa LIKE ?
    """, (f"%{keyword}%",)*4)

    data = cur.fetchall()
    conn.close()
    return data


# ==============================
# SEARCH SINH HOẠT
# ==============================
def search_sinhhoat(keyword):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT ma_hd, ten_hd, ngay, dia_diem, noi_dung
        FROM HoatDong
        WHERE ma_hd LIKE ?
        OR ten_hd LIKE ?
        OR dia_diem LIKE ?
    """, (f"%{keyword}%",)*3)

    data = cur.fetchall()
    conn.close()
    return data


# ==============================
# SEARCH ĐOÀN PHÍ
# ==============================
def search_doanphi(keyword):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT 
            dp.ma_dv,
            dv.ho_ten,
            dp.thang,
            dp.so_tien,
            dp.ngay_dong,
            dp.trang_thai
        FROM DoanPhi dp
        JOIN DoanVien dv ON dp.ma_dv = dv.ma_dv
        WHERE 
            dp.ma_dv LIKE ?
            OR dv.ho_ten LIKE ?
            OR dp.trang_thai LIKE ?
    """, (f"%{keyword}%",)*3)

    data = cur.fetchall()
    conn.close()
    return data