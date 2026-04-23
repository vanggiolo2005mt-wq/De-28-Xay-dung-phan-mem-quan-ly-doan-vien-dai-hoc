from database.db_helper import get_connection


def get_doanphi(khoa="Tất cả", lop="Tất cả", thang=None):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT 
        dv.ma_dv,
        dv.ho_ten,
        cd.ten_lop,
        k.ten_khoa,
        dp.trang_thai,
        dp.ngay_dong,
        dp.thang
    FROM DoanPhi dp
    JOIN DoanVien dv ON dp.ma_dv = dv.ma_dv
    JOIN ChiDoan cd ON dv.ma_lop = cd.ma_lop
    JOIN Khoa k ON cd.ma_khoa = k.ma_khoa
    WHERE 1=1
    """

    params = []

    if khoa != "Tất cả":
        query += " AND k.ten_khoa = ?"
        params.append(khoa)

    if lop != "Tất cả":
        query += " AND cd.ten_lop = ?"
        params.append(lop)

    if thang and thang != "Tất cả":
        query += " AND dp.thang = ?"
        params.append(int(thang))

    cursor.execute(query, params)
    data = cursor.fetchall()
    conn.close()

    return data


# =============================
# UPDATE 1 DÒNG
# =============================
def update_trangthai(ma_dv, thang, trangthai):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE DoanPhi
        SET trang_thai = ?
        WHERE ma_dv = ? AND thang = ?
    """, (trangthai, ma_dv, thang))

    conn.commit()
    conn.close()