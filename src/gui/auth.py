import hashlib
from models.user_model import UserModel


class AuthController:
    def __init__(self):
        self.model = UserModel()

    def login(self, username, password):
        users = self.model.get_all_users()

        pw_hash = hashlib.sha256(password.encode().strip()).hexdigest()

        for u in users:
            if u["username"] == username and u.get("password") == pw_hash:
                return {
                    "status": True,
                    "user": u
                }

        return {
            "status": False,
            "message": "Sai tài khoản hoặc mật khẩu"
        }