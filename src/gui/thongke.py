from PyQt5.QtWidgets import QTableWidgetItem
from datetime import datetime
from models.thongke_model import ThongKeModel


class ThongKeController:

    def __init__(self, ui):
        self.ui = ui
        self.model = ThongKeModel()

        self.load_filter()

        self.ui.cbMonth.currentIndexChanged.connect(self.thong_ke)
        self.ui.cbYear.currentIndexChanged.connect(self.thong_ke)
        self.ui.btnThongKe.clicked.connect(self.thong_ke)

        self.thong_ke()

    def load_filter(self):
        for i in range(1, 13):
            self.ui.cbMonth.addItem(str(i))

        for y in range(2024, 2031):
            self.ui.cbYear.addItem(str(y))

        now = datetime.now()
        self.ui.cbMonth.setCurrentText(str(now.month))
        self.ui.cbYear.setCurrentText(str(now.year))

    def thong_ke(self):
        thang = int(self.ui.cbMonth.currentText())
        nam = int(self.ui.cbYear.currentText())

        data = self.model.get_doan_phi(thang, nam)

        tong = len(data)
        da_dong = 0
        tong_thu = 0

        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ["Mã DV", "Họ tên", "Lớp", "Khoa", "Trạng thái"]
        )

        for row in data:
            # ✅ FIX CHÍNH Ở ĐÂY
            ma_dv, ten, lop, khoa, trang_thai, so_tien = row

            r = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(r)

            self.ui.tableWidget.setItem(r, 0, QTableWidgetItem(ma_dv))
            self.ui.tableWidget.setItem(r, 1, QTableWidgetItem(ten))
            self.ui.tableWidget.setItem(r, 2, QTableWidgetItem(lop))
            self.ui.tableWidget.setItem(r, 3, QTableWidgetItem(khoa))

            status = "Đã đóng" if trang_thai == "Da dong" else "Chưa đóng"
            self.ui.tableWidget.setItem(r, 4, QTableWidgetItem(status))

            # ===== STATS =====
            if trang_thai == "Da dong":
                da_dong += 1
                tong_thu += so_tien

        # ===== TỶ LỆ =====
        ty_le = (da_dong / tong * 100) if tong > 0 else 0

        # ===== SINH HOẠT (tạm) =====
        ty_le_sinh_hoat = 0

        # ===== LABEL =====
        self.ui.lblTongDV.setText(f"Tổng: {tong}")
        self.ui.lblDaDong.setText(f"Đã đóng: {da_dong}")
        self.ui.lblTyLe.setText(f"Tỷ lệ đóng: {ty_le:.1f}%")
        self.ui.lblSinhHoat.setText(f"Sinh hoạt: {ty_le_sinh_hoat}%")
        self.ui.lblTongThu.setText(f"Tổng thu: {tong_thu:,} đ")