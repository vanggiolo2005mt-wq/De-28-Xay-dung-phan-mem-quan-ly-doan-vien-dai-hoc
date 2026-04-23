from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt

from models import dashboard_model


class DashboardController:
    def __init__(self, ui):
        self.ui = ui
        self.load_data()

    def load_data(self):
        stats = dashboard_model.get_stats()

        # ===== STATS =====
        self.ui.lblTongDV.setText(str(stats["tong"]))
        self.ui.lblChuaDong.setText(str(stats["chua_dong"]))
        self.ui.lblDangHD.setText(str(stats["dang_hd"]))
        self.ui.lblTyLe.setText(stats["ty_le"])

        # ===== HOẠT ĐỘNG =====
        data = dashboard_model.get_recent_activities()

        self.ui.tableWidget.setRowCount(0)

        for row_data in data:
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)

            for col, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.tableWidget.setItem(row, col, item)