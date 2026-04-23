import sys
import os
from PyQt5.QtWidgets import QApplication
from gui.auth import AuthController
from gui.main_window import MainWindow
# Để import được các module trong src/database và src/gui
from database.init_db import create_tables


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    create_tables()  # Tạo các bảng trong cơ sở dữ liệu

    window = MainWindow()
    window.showMaximized()

    sys.exit(app.exec_())