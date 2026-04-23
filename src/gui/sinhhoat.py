from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QCheckBox
from PyQt5.QtCore import Qt

from models.sinhhoat_model import (
    get_all_hoatdong,
    insert_hoatdong,
    update_hoatdong,
    delete_hoatdong
)

from models.chidoan_model import get_all_chidoan


class SinhHoatController:
    def __init__(self, ui):
        self.ui = ui

        self.load_combo()
        self.load_data()
        self.connect_event()

    # =========================
    # EVENT
    # =========================
    def connect_event(self):
        self.ui.btnThem.clicked.connect(self.them)
        self.ui.btnSua.clicked.connect(self.sua)
        self.ui.btnXoa.clicked.connect(self.xoa)
        self.ui.btnRefresh.clicked.connect(self.reset)

        self.ui.tableHoatDong.itemSelectionChanged.connect(self.fill_form)

        self.ui.btnCheckAll.clicked.connect(self.check_all)
        self.ui.btnUncheckAll.clicked.connect(self.uncheck_all)
        self.ui.btnLuuDiemDanh.clicked.connect(self.save_diemdanh)

    # =========================
    # COMBO KHỚP UI
    # =========================
    def load_combo(self):
        # KHOA (UI có sẵn)
        self.ui.comboKhoa.setCurrentIndex(0)

        # LỚP (từ DB)
        self.ui.comboLop.clear()
        self.ui.comboLop.addItem("Tất cả")

        for ma, ten, *_ in get_all_chidoan():
            self.ui.comboLop.addItem(ten, ma)

    # =========================
    # LOAD HOẠT ĐỘNG
    # =========================
    def load_data(self):
        data = get_all_hoatdong()

        self.ui.tableHoatDong.setRowCount(0)

        for row_data in data:
            row = self.ui.tableHoatDong.rowCount()
            self.ui.tableHoatDong.insertRow(row)

            for col, value in enumerate(row_data):
                self.ui.tableHoatDong.setItem(
                    row, col,
                    QTableWidgetItem(str(value))
                )

    # =========================
    # FILL FORM
    # =========================
    def fill_form(self):
        row = self.ui.tableHoatDong.currentRow()
        if row < 0:
            return

        self.ui.lineEdit_ma.setText(self.ui.tableHoatDong.item(row, 0).text())
        self.ui.lineEdit_ten.setText(self.ui.tableHoatDong.item(row, 1).text())
        self.ui.lineEdit_diadiem.setText(self.ui.tableHoatDong.item(row, 3).text())
        self.ui.lineEdit_noidung.setText(self.ui.tableHoatDong.item(row, 4).text())

    # =========================
    # THÊM
    # =========================
    def them(self):
        ma = self.ui.lineEdit_ma.text().strip()
        ten = self.ui.lineEdit_ten.text().strip()
        diadiem = self.ui.lineEdit_diadiem.text().strip()
        noidung = self.ui.lineEdit_noidung.text().strip()
        ngay = self.ui.dateEdit.date().toString("yyyy-MM-dd")

        if not ma or not ten:
            QMessageBox.warning(self.ui, "Lỗi", "Thiếu dữ liệu!")
            return

        insert_hoatdong(ma, ten, ngay, diadiem, noidung)

        self.load_data()
        self.reset()

    # =========================
    # SỬA
    # =========================
    def sua(self):
        ma = self.ui.lineEdit_ma.text().strip()
        ten = self.ui.lineEdit_ten.text().strip()
        diadiem = self.ui.lineEdit_diadiem.text().strip()
        noidung = self.ui.lineEdit_noidung.text().strip()
        ngay = self.ui.dateEdit.date().toString("yyyy-MM-dd")

        if not ma:
            return

        update_hoatdong(ma, ten, ngay, diadiem, noidung)

        self.load_data()

    # =========================
    # XÓA
    # =========================
    def xoa(self):
        row = self.ui.tableHoatDong.currentRow()
        if row < 0:
            return

        ma = self.ui.tableHoatDong.item(row, 0).text()
        delete_hoatdong(ma)

        self.load_data()

    # =========================
    # RESET FORM
    # =========================
    def reset(self):
        self.ui.lineEdit_ma.clear()
        self.ui.lineEdit_ten.clear()
        self.ui.lineEdit_diadiem.clear()
        self.ui.lineEdit_noidung.clear()

    # =========================
    # ĐIỂM DANH (UI KHỚP 100%)
    # =========================
    def check_all(self):
        for row in range(self.ui.tableDiemDanh.rowCount()):
            cb = QCheckBox()
            cb.setChecked(True)
            self.ui.tableDiemDanh.setCellWidget(row, 4, cb)

    def uncheck_all(self):
        for row in range(self.ui.tableDiemDanh.rowCount()):
            cb = QCheckBox()
            cb.setChecked(False)
            self.ui.tableDiemDanh.setCellWidget(row, 4, cb)

    def save_diemdanh(self):
        QMessageBox.information(self.ui, "OK", "Đã lưu điểm danh (demo)")