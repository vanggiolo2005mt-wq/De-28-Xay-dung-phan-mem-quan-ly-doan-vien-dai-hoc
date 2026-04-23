from PyQt5.QtWidgets import QTableWidgetItem
from models.doanvien_model import get_all_doanvien


class DoanVienController:
    def __init__(self, ui):
        self.ui = ui
        self.setup_table()
        self.load_data()

    # =========================
    # SETUP TABLE
    # =========================
    def setup_table(self):
        self.ui.tableDoanVien.setColumnCount(7)
        self.ui.tableDoanVien.setHorizontalHeaderLabels([
            "Mã DV", "Họ tên", "Ngày sinh",
            "Lớp", "Khoa", "Ngày vào Đoàn", "Trạng thái"
        ])

    # =========================
    # LOAD DATA
    # =========================
    def load_data(self):
        data = get_all_doanvien()

        self.ui.tableDoanVien.setRowCount(0)

        if not data:
            return

        for row_data in data:
            row = self.ui.tableDoanVien.rowCount()
            self.ui.tableDoanVien.insertRow(row)

            for col, value in enumerate(row_data):
                item = QTableWidgetItem(str(value) if value is not None else "")
                self.ui.tableDoanVien.setItem(row, col, item)

        # 👉 optional: chỉ cần nếu UI lag (không bắt buộc)
        self.ui.tableDoanVien.resizeColumnsToContents()
        