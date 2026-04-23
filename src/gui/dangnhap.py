import os
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from gui.auth import AuthController


class DangNhap(QDialog):
    def __init__(self):
        super().__init__()

        ui_path = os.path.join(os.path.dirname(__file__), "ui", "dangnhap.ui")
        ui_path = os.path.normpath(ui_path)

        uic.loadUi(ui_path, self)

        self.controller = AuthController()
        self.current_user = None

        # events
        self.btnLogin.clicked.connect(self.handle_login)
        self.txtPassword.returnPressed.connect(self.handle_login)

    def handle_login(self):
        username = self.txtUsername.text().strip()
        password = self.txtPassword.text().strip()

        result = self.controller.login(username, password)

        if result["status"]:
            self.current_user = result["user"]

            self.lblStatus.setText("✅ Đăng nhập thành công")
            self.lblStatus.setStyleSheet("color:green;")

            self.accept()
        else:
            self.lblStatus.setText("❌ " + result["message"])
            self.lblStatus.setStyleSheet("color:red;")
            self.txtPassword.clear()