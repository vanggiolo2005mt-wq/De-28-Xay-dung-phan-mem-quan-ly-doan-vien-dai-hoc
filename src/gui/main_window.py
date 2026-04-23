from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QMessageBox
import hashlib
import json
import os

from gui.dashboard import DashboardController
from gui.doanvien import DoanVienController
from gui.doanphi import DoanPhiController
from gui.sinhhoat import SinhHoatController
from gui.timkiem import TimKiem
from gui.thongke import ThongKeController
from gui.dangnhap import DangNhap
from gui.user import UserController
from gui.auth import AuthController
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        ui_path = os.path.join(os.path.dirname(__file__), "ui", "Trangchu.ui")
        uic.loadUi(ui_path, self)

        self.pages = {}

        # ===== DASHBOARD =====
        self.pages["dashboard"] = QWidget()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui", "dashboard.ui"), self.pages["dashboard"])
        self.dashboard = DashboardController(self.pages["dashboard"])
        self.idx_dashboard = self.stackedWidget_3.addWidget(self.pages["dashboard"])
        # ===== USER MANAGEMENT =====
        self.pages["user"] = QWidget()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui", "user.ui"), self.pages["user"])
        self.user_controller = UserController(self.pages["user"])
        self.idx_user = self.stackedWidget_3.addWidget(self.pages["user"])

        # ===== DOAN VIEN =====
        self.pages["doanvien"] = QWidget()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui", "doanvien.ui"), self.pages["doanvien"])
        self.doanvien = DoanVienController(self.pages["doanvien"])
        self.idx_doanvien = self.stackedWidget_3.addWidget(self.pages["doanvien"])

        # ===== DOAN PHI =====
# ===== DOAN PHI =====
        self.pages["doanphi"] = QWidget()

        uic.loadUi(
       os.path.join(os.path.dirname(__file__), "ui", "doanphi.ui"),
         self.pages["doanphi"]
)

# ADD PAGE
        self.idx_doanphi = self.stackedWidget_3.addWidget(self.pages["doanphi"])

# SET CONTROLLER
        self.doanphi = DoanPhiController(self.pages["doanphi"])

# 👉 QUAN TRỌNG: hiển thị page
        self.stackedWidget_3.setCurrentWidget(self.pages["doanphi"]) 
        # ===== SINH HOAT =====
        self.pages["sinhhoat"] = QWidget()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui", "sinhhoat.ui"), self.pages["sinhhoat"])
        self.sinhhoat = SinhHoatController(self.pages["sinhhoat"])
        self.idx_sinhhoat = self.stackedWidget_3.addWidget(self.pages["sinhhoat"])

        # ===== TIM KIEM =====
        self.pages["timkiem"] = QWidget()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui", "TimKiem.ui"), self.pages["timkiem"])
        self.timkiem = TimKiem(self.pages["timkiem"])
        self.idx_timkiem = self.stackedWidget_3.addWidget(self.pages["timkiem"])

        # ===== THONG KE =====
        self.pages["thongke"] = QWidget()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui", "ThongKe.ui"), self.pages["thongke"])
        self.thongke = ThongKeController(self.pages["thongke"])
        self.idx_thongke = self.stackedWidget_3.addWidget(self.pages["thongke"])

        # ===== MENU =====
        self.btnDashboard_3.clicked.connect(lambda: self.switch_page(self.idx_dashboard))
        self.btnUser_3.clicked.connect(lambda: self.switch_page(self.idx_user))
        self.btnDoanVien_3.clicked.connect(lambda: self.switch_page(self.idx_doanvien))
        self.btnSinhHoat_3.clicked.connect(lambda: self.switch_page(self.idx_sinhhoat))
        self.btnDoanPhi_3.clicked.connect(lambda: self.switch_page(self.idx_doanphi))
        self.btnTimKiem_3.clicked.connect(lambda: self.switch_page(self.idx_timkiem))
        self.btnThongKe_3.clicked.connect(lambda: self.switch_page(self.idx_thongke))
        self.btnLogout_3.clicked.connect(self.logout)

        self.switch_page(self.idx_dashboard)

        # ===== LOGIN CONTROL =====
        self.login_shown = False
        self.overlay = None
        self.login_widget = None

    # ================= OVERLAY =================
    def create_overlay(self):
        self.overlay = QWidget(self)
        self.overlay.setStyleSheet("background-color: rgba(0,0,0,120);")
        self.overlay.setGeometry(self.rect())
        self.overlay.hide()

    def resizeEvent(self, event):
        super().resizeEvent(event)

        if self.overlay:
            self.overlay.setGeometry(self.rect())

        if self.login_widget:
            self.login_widget.setGeometry(self.rect())

    def lock_ui(self):
        if self.overlay:
            self.overlay.setGeometry(self.rect())
            self.overlay.show()
            self.overlay.raise_()

    def unlock_ui(self):
        if self.overlay:
            self.overlay.hide()

    # ================= LOGIN =================
    def show_login_overlay(self):
        if self.login_shown:
            return

        self.login_shown = True

        self.login_widget = DangNhap()
        self.login_widget.setParent(self)
        self.login_widget.setWindowFlags(Qt.FramelessWindowHint | Qt.Widget)
        self.login_widget.setGeometry(self.rect())

        self.login_widget.btnLogin.clicked.connect(self.handle_login)

        self.lock_ui()
        self.login_widget.show()
        self.login_widget.raise_()

    def handle_login(self):
        username = self.login_widget.txtUsername.text().strip()
        password = self.login_widget.txtPassword.text().strip()

        controller = AuthController()
        result = controller.login(username, password)

        if result["status"]:
           QMessageBox.information(self, "OK", "Đăng nhập thành công")

           self.current_user = result["user"]   # 🔥 LƯU USER

           self.login_widget.close()
           self.unlock_ui()

        # 👉 HIỂN THỊ USER
           self.lblUser_3.setText(f"Xin chào: {self.current_user['username']}")

        # 👉 PHÂN QUYỀN
           self.apply_role()

        else:
            QMessageBox.warning(self, "Lỗi", result["message"])
    
    def apply_role(self):
        role =self.current_user.get("role", "")

        if role !="ADMIN":
            self.btnUser_3.hide()
    # ================= SHOW EVENT =================
    def showEvent(self, event):
        super().showEvent(event)

        if not self.overlay:
            self.create_overlay()

        self.show_login_overlay()

    # ================= SWITCH PAGE =================
    def switch_page(self, index):
        self.stackedWidget_3.setCurrentIndex(index)

        if index == self.idx_dashboard:
            self.dashboard.load_data()

    # ================= LOGOUT =================
    def logout(self):
        reply = QMessageBox.question(
            self,
            "Đăng xuất",
            "Bạn có chắc muốn đăng xuất?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            self.close()