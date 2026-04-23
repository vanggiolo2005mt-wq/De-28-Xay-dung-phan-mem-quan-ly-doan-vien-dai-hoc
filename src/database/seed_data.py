from db_helper import get_connection


# =============================
# XÓA DATA CŨ
# =============================
def clear_data():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = OFF;")

    cursor.executescript("""
    DELETE FROM DiemDanh;
    DELETE FROM DoanPhi;
    DELETE FROM PhanCong;
    DELETE FROM DoanVien;
    DELETE FROM HoatDong;
    DELETE FROM ChiDoan;
    DELETE FROM Khoa;
    DELETE FROM Task;
    """)

    conn.commit()

    cursor.execute("PRAGMA foreign_keys = ON;")

    conn.close()
# =============================
# KHOA
# =============================
def seed_khoa():
    conn = get_connection()
    cursor = conn.cursor()

    data = [
        ("CNTT", "Công nghệ thông tin"),
        ("KT", "Kinh tế"),
        ("QTKD", "Quản trị kinh doanh"),
        ("TCNH", "Tài chính - Ngân hàng"),
        ("CK", "Cơ khí"),
        ("DT", "Điện - Điện tử"),
        ("OTO", "Công nghệ ô tô"),
        ("XD", "Xây dựng"),
        ("NN", "Ngôn ngữ Anh"),
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO Khoa (ma_khoa, ten_khoa)
        VALUES (?, ?)
    """, data)

    conn.commit()
    conn.close()


# =============================
# CHI ĐOÀN
# =============================
def seed_chidoan():
    conn = get_connection()
    cursor = conn.cursor()

    data = [
        ("CNTT1", "CNTT1", "CNTT"),
        ("CNTT2", "CNTT2", "CNTT"),
        ("CNTT3", "CNTT3", "CNTT"),
        ("KT1", "KT1", "KT"),
        ("KT2", "KT2", "KT"),
        ("QTKD1", "QTKD1", "QTKD"),
        ("TCNH1", "TCNH1", "TCNH"),
        ("CK1", "CK1", "CK"),
        ("DT1", "DT1", "DT"),
        ("OTO1", "OTO1", "OTO"),
        ("XD1", "XD1", "XD"),
        ("NN1", "NN1", "NN"),
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO ChiDoan (ma_lop, ten_lop, ma_khoa)
        VALUES (?, ?, ?)
    """, data)

    conn.commit()
    conn.close()


# =============================
# ĐOÀN VIÊN
# =============================
def seed_doanvien():
    conn = get_connection()
    cursor = conn.cursor()

    data = [
        ("DV001", "Nguyễn Minh Anh", "2004-01-01", "Nam", "CNTT1", "2022-01-01", "Hoat dong"),
        ("DV002", "Trần Quốc Bảo", "2004-02-12", "Nam", "CNTT2", "2022-01-01", "Hoat dong"),
        ("DV003", "Lê Hoàng Nam", "2004-03-23", "Nam", "CNTT3", "2022-01-01", "Hoat dong"),
        ("DV004", "Phạm Thu Trang", "2004-04-04", "Nu", "CNTT1", "2022-01-01", "Ngung"),

        ("DV005", "Hoàng Gia Huy", "2004-05-15", "Nam", "KT1", "2022-01-01", "Hoat dong"),
        ("DV006", "Đặng Quỳnh Anh", "2004-06-06", "Nu", "KT2", "2022-01-01", "Hoat dong"),
        ("DV007", "Bùi Đức Anh", "2004-07-17", "Nam", "KT1", "2022-01-01", "Ngung"),
        ("DV008", "Phan Minh Tuấn", "2004-08-08", "Nam", "KT2", "2022-01-01", "Hoat dong"),

        ("DV009", "Vũ Thanh Tùng", "2004-09-19", "Nam", "QTKD1", "2022-01-01", "Hoat dong"),
        ("DV010", "Ngô Thị Lan", "2004-10-10", "Nu", "QTKD1", "2022-01-01", "Hoat dong"),

        ("DV011", "Nguyễn Văn Hùng", "2004-11-11", "Nam", "TCNH1", "2022-01-01", "Hoat dong"),
        ("DV012", "Trần Thị Mai", "2004-12-12", "Nu", "TCNH1", "2022-01-01", "Ngung"),

        ("DV013", "Lê Quang Huy", "2004-01-13", "Nam", "CK1", "2022-01-01", "Hoat dong"),
        ("DV014", "Phạm Đức Long", "2004-02-14", "Nam", "CK1", "2022-01-01", "Hoat dong"),

        ("DV015", "Hoàng Thị Hoa", "2004-03-15", "Nu", "DT1", "2022-01-01", "Hoat dong"),
        ("DV016", "Đặng Văn Nam", "2004-04-16", "Nam", "DT1", "2022-01-01", "Ngung"),

        ("DV017", "Bùi Thị Hương", "2004-05-17", "Nu", "OTO1", "2022-01-01", "Hoat dong"),
        ("DV018", "Phan Quốc Việt", "2004-06-18", "Nam", "OTO1", "2022-01-01", "Hoat dong"),

        ("DV019", "Vũ Minh Đức", "2004-07-19", "Nam", "XD1", "2022-01-01", "Hoat dong"),
        ("DV020", "Ngô Thanh Bình", "2004-08-20", "Nam", "NN1", "2022-01-01", "Hoat dong"),
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO DoanVien
        (ma_dv, ho_ten, ngay_sinh, gioi_tinh, ma_lop, ngay_vao_doan, trang_thai)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, data)

    conn.commit()
    conn.close()


# =============================
# HOẠT ĐỘNG
# =============================
def seed_hoatdong():
    conn = get_connection()
    cursor = conn.cursor()

    data = [
        ("HD01", "Sinh hoạt tháng 1", "2026-01-05", "Hội trường A", "Họp chi đoàn"),
        ("HD02", "Hiến máu", "2026-03-10", "Bệnh viện B", "Thiện nguyện"),
        ("HD03", "Trồng cây", "2026-04-15", "Sân trường", "Môi trường"),
        ("HD04", "Bóng đá", "2026-05-10", "Sân vận động", "Thể thao"),
        ("HD05", "Workshop", "2026-03-18", "Phòng 101", "Kỹ năng"),
        ("HD06", "Seminar", "2026-03-22", "Phòng 202", "Học tập"),
        ("HD07", "Văn nghệ", "2026-02-01", "Hội trường", "Giải trí"),
        ("HD08", "Tham quan", "2026-04-05", "Doanh nghiệp", "Trải nghiệm"),
        ("HD09", "Tuyên truyền", "2026-03-20", "Sân trường", "Giáo dục"),
        ("HD10", "Ngày hội SV", "2026-06-01", "Toàn trường", "Sự kiện"),
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO HoatDong
        (ma_hd, ten_hd, ngay, dia_diem, noi_dung)
        VALUES (?, ?, ?, ?, ?)
    """, data)

    conn.commit()
    conn.close()


# =============================
# ĐOÀN PHÍ
# =============================
def seed_doanphi():
    conn = get_connection()
    cursor = conn.cursor()

    data = []

    for i in range(1, 21):
        ma = f"DV{str(i).zfill(3)}"
        data.append((
            ma, 1, 2026, 50000,
            "Da dong" if i % 2 == 0 else "Chua dong",
            f"01/01/2026" if i % 2 == 0 else None
        ))

    cursor.executemany("""
        INSERT OR IGNORE INTO DoanPhi
        (ma_dv, thang, nam, so_tien, trang_thai, ngay_dong)
        VALUES (?, ?, ?, ?, ?, ?)
    """, data)
    
    conn.commit()
    conn.close()


# =============================
# RUN ALL
# =============================
def seed_all():
    clear_data()
    seed_khoa()
    seed_chidoan()
    seed_doanvien()
    seed_hoatdong()
    seed_doanphi()

if __name__ == "__main__":
    seed_all()
    print("✅ SEED FULL CHUẨN HOÀN THÀNH")