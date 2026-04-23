from models.user_model import UserModel
from PyQt5.QtWidgets import QMessageBox


class UserController:
    def __init__(self, ui):
        self.ui = ui
        self.model = UserModel()

        # ===== EVENTS =====
        self.ui.btnAdd.clicked.connect(self.handle_add)
        self.ui.btnRefresh.clicked.connect(self.load_users)

        # load data ban đầu
        self.load_users()

    # ===== CREATE USER =====
    def create_user(self, username, password, role):
        if not username or not password:
            return False, "Không được để trống"

        success, msg = self.model.add_user(username, password, role)
        return success, msg

    # ===== HANDLE ADD (UI) =====
    def handle_add(self):
        username = self.ui.txtUsername.text().strip()
        password = self.ui.txtPassword.text().strip()
        role = self.ui.cboRole.currentText()

        success, msg = self.create_user(username, password, role)

        if success:
            QMessageBox.information(self.ui, "OK", msg)
            self.load_users()
        else:
            QMessageBox.warning(self.ui, "Lỗi", msg)

    # ===== LOAD USERS =====
    def load_users(self):
        users = self.model.get_all_users()

        self.ui.tableUser.setRowCount(len(users))

        for row, u in enumerate(users):
            self.ui.tableUser.setItem(row, 0, self._item(u["id"]))
            self.ui.tableUser.setItem(row, 1, self._item(u["username"]))
            self.ui.tableUser.setItem(row, 2, self._item(u["role"]))

    def _item(self, text):
        from PyQt5.QtWidgets import QTableWidgetItem
        return QTableWidgetItem(str(text))