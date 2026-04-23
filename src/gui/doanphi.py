from PyQt5.QtWidgets import QTableWidgetItem
from models.doanphi_model import get_doanphi, update_trangthai
from PyQt5.QtCore import Qt


class DoanPhiController:
    def __init__(self, ui):
        self.ui = ui

        self.load_combo()
        self.load_data()

        self.ui.btnCheckAll.clicked.connect(self.check_all)
        self.ui.btnUncheckAll.clicked.connect(self.uncheck_all)
        self.ui.btnLuu.clicked.connect(self.load_data)

        self.ui.comboKhoa.currentTextChanged.connect(self.load_data)
        self.ui.comboLop.currentTextChanged.connect(self.load_data)
        self.ui.comboThang.currentTextChanged.connect(self.load_data)

    # =============================
    # COMBO
    # =============================
    def load_combo(self):
        self.ui.comboKhoa.addItems(["Tất cả", "Công nghệ thông tin", "Kinh tế"])
        self.ui.comboLop.addItems(["Tất cả"])
        self.ui.comboThang.addItems(["Tất cả"] + [str(i) for i in range(1, 13)])

    # =============================
    # LOAD TABLE (DỮ LIỆU THẬT)
    # =============================
    def load_data(self):
        khoa = self.ui.comboKhoa.currentText()
        lop = self.ui.comboLop.currentText()
        thang = self.ui.comboThang.currentText()

        data = get_doanphi(khoa, lop, thang)

        self.ui.tableDoanPhi.setRowCount(0)

        for row_data in data:
            row = self.ui.tableDoanPhi.rowCount()
            self.ui.tableDoanPhi.insertRow(row)

            # 6 cột theo UI
            for col, value in enumerate(row_data):
                self.ui.tableDoanPhi.setItem(row, col, QTableWidgetItem(str(value)))


    # =============================
    # CHECK ALL
    # =============================
    def check_all(self):
        for r in range(self.ui.tableDoanPhi.rowCount()):
            self.ui.tableDoanPhi.setItem(r, 4, QTableWidgetItem("Đã đóng"))

    # =============================
    # UNCHECK ALL
    # =============================
    def uncheck_all(self):
        for r in range(self.ui.tableDoanPhi.rowCount()):
            self.ui.tableDoanPhi.setItem(r, 4, QTableWidgetItem("Chưa đóng"))

    # =============================
    # SAVE (ghi DB thật)
    # =============================
def load_data(self):
    khoa = self.ui.comboKhoa.currentText()
    lop = self.ui.comboLop.currentText()
    thang = self.ui.comboThang.currentText()

    data = get_doanphi(khoa, lop, thang)

    self.ui.tableDoanPhi.setRowCount(0)

    for row_data in data:
        row = self.ui.tableDoanPhi.rowCount()
        self.ui.tableDoanPhi.insertRow(row)

        for col, value in enumerate(row_data):
            self.ui.tableDoanPhi.setItem(row, col, QTableWidgetItem(str(value)))


def save(self):
    for r in range(self.ui.tableDoanPhi.rowCount()):
        ma_item = self.ui.tableDoanPhi.item(r, 0)
        tt_item = self.ui.tableDoanPhi.item(r, 4)

        if not ma_item or not tt_item:
            continue

        ma = ma_item.text()
        trangthai = tt_item.text()
        thang = int(self.ui.comboThang.currentText())

        update_trangthai(ma, thang, trangthai)