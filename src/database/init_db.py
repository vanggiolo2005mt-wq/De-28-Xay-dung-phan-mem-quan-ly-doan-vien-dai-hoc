from database.db_helper import get_connection


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # =========================
    # KHOA
    # =========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Khoa (
        ma_khoa TEXT PRIMARY KEY,
        ten_khoa TEXT NOT NULL
    )
    """)

    # =========================
    # CHI ĐOÀN
    # =========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ChiDoan (
        ma_lop TEXT PRIMARY KEY,
        ten_lop TEXT NOT NULL,
        ma_khoa TEXT NOT NULL,
        FOREIGN KEY (ma_khoa) REFERENCES Khoa(ma_khoa)
            ON DELETE CASCADE
    )
    """)

    # =========================
    # ĐOÀN VIÊN
    # =========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS DoanVien (
        ma_dv TEXT PRIMARY KEY,
        ho_ten TEXT NOT NULL,
        ngay_sinh TEXT,
        gioi_tinh TEXT,
        ma_lop TEXT NOT NULL,
        ngay_vao_doan TEXT,
        trang_thai TEXT DEFAULT 'Hoat dong',

        FOREIGN KEY (ma_lop) REFERENCES ChiDoan(ma_lop)
            ON DELETE CASCADE
    )
    """)

    # =========================
    # HOẠT ĐỘNG
    # =========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS HoatDong (
        ma_hd TEXT PRIMARY KEY,
        ten_hd TEXT,
        ngay TEXT,
        dia_diem TEXT,
        noi_dung TEXT
    )
    """)

    # =========================
    # TASK (NHIỆM VỤ)
    # =========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Task (
        ma_task INTEGER PRIMARY KEY AUTOINCREMENT,
        ten_task TEXT NOT NULL,
        mo_ta TEXT,
        muc_do TEXT DEFAULT 'Binh thuong'
    )
    """)

    # =========================
    # PHÂN CÔNG NHIỆM VỤ
    # =========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS PhanCong (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ma_hd TEXT NOT NULL,
        ma_dv TEXT NOT NULL,
        ma_task INTEGER NOT NULL,
        trang_thai TEXT DEFAULT 'Chua thuc hien',

        FOREIGN KEY (ma_hd) REFERENCES HoatDong(ma_hd)
            ON DELETE CASCADE,

        FOREIGN KEY (ma_dv) REFERENCES DoanVien(ma_dv)
            ON DELETE CASCADE,

        FOREIGN KEY (ma_task) REFERENCES Task(ma_task)
            ON DELETE CASCADE
    )
    """)

    # =========================
    # ĐIỂM DANH
    # =========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS DiemDanh (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ma_hd TEXT NOT NULL,
        ma_dv TEXT NOT NULL,
        co_mat INTEGER DEFAULT 0 CHECK (co_mat IN (0,1)),
        ghi_chu TEXT,

        FOREIGN KEY (ma_hd) REFERENCES HoatDong(ma_hd)
            ON DELETE CASCADE,

        FOREIGN KEY (ma_dv) REFERENCES DoanVien(ma_dv)
            ON DELETE CASCADE,

        UNIQUE(ma_hd, ma_dv)
    )
    """)

    # =========================
    # ĐOÀN PHÍ
    # =========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS DoanPhi (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ma_dv TEXT NOT NULL,
        thang INTEGER NOT NULL,
        nam INTEGER NOT NULL,
        so_tien INTEGER DEFAULT 50000,
        trang_thai TEXT DEFAULT 'Chua dong',
        ngay_dong TEXT,

        FOREIGN KEY (ma_dv) REFERENCES DoanVien(ma_dv),
        UNIQUE(ma_dv, thang, nam)
    )
    """)
    # =========================
# USER (TÀI KHOẢN)
# =========================
    cursor.execute("""
CREATE TABLE IF NOT EXISTS User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT 'USER'
)
""")
    cursor.execute("SELECT * FROM User WHERE role='ADMIN'")
    admin = cursor.fetchone()

    if not admin:
        cursor.execute("""
            INSERT INTO User (username, password, role)
            VALUES (?, ?, ?)
        """, ("admin", "123456", "ADMIN"))

    conn.commit()
    conn.close()


# =========================
# MAIN RUN
# =========================
if __name__ == "__main__":
    create_tables()
    print("✅ DATABASE FULL CHUẨN ĐÃ TẠO XONG")