from PyQt5.QtWidgets import QTableWidgetItem
from models.timkiem_model import (
    search_doanvien,
    search_sinhhoat,
    search_doanphi
)


class TimKiem:
    def __init__(self, ui):
        self.ui = ui

        self.ui.btnSearch.clicked.connect(self.search)
        self.ui.txtSearch.textChanged.connect(self.search)
        self.ui.btnReset.clicked.connect(self.reset)

    # ================= SEARCH =================
    def search(self):
        keyword = self.ui.txtSearch.text().strip()

        index = self.ui.tabWidget.currentIndex()

        # reset nếu rỗng
        if not keyword:
            self.reset()
            return

        if index == 0:
            data = search_doanvien(keyword)
            self.fill_table(self.ui.tblDoanVien, data)

        elif index == 1:
            data = search_sinhhoat(keyword)
            self.fill_table(self.ui.tblSinhHoat, data)

        elif index == 2:
            data = search_doanphi(keyword)
            self.fill_table(self.ui.tblDoanPhi, data)

    # ================= FILL TABLE =================
    def fill_table(self, table, data):
        table.setRowCount(0)

        for row_data in data:
            row = table.rowCount()
            table.insertRow(row)

            for col, value in enumerate(row_data):
                table.setItem(row, col, QTableWidgetItem(str(value)))

    # ================= RESET =================
    def reset(self):
        self.ui.txtSearch.clear()

        for table in [
            self.ui.tblDoanVien,
            self.ui.tblSinhHoat,
            self.ui.tblDoanPhi
        ]:
            table.setRowCount(0)