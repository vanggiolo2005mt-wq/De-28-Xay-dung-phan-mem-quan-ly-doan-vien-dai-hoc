from database.db_helper import get_connection


class ThongKeModel:

    def get_doan_phi(self, thang, nam):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT 
            dv.ma_dv,
            dv.ho_ten,
            cd.ten_lop,
            k.ten_khoa,
            dp.trang_thai,
            dp.so_tien
        FROM DoanPhi dp
        JOIN DoanVien dv ON dv.ma_dv = dp.ma_dv
        JOIN ChiDoan cd ON cd.ma_lop = dv.ma_lop
        JOIN Khoa k ON k.ma_khoa = cd.ma_khoa
        WHERE dp.thang = ? AND dp.nam = ?
        """

        cursor.execute(query, (thang, nam))
        data = cursor.fetchall()

        conn.close()
        return data