import os
import json
import hashlib


class UserModel:
    def __init__(self):
        self.data_path = os.path.join(
            os.path.dirname(__file__), "..", "data", "users.json"
        )

        # 🔥 đảm bảo file tồn tại
        if not os.path.exists(self.data_path):
            self.save_users([])
        self.ensure_admin()   
    # ===== HASH =====
    def hash_pw(self, pw):
        return hashlib.sha256(pw.encode()).hexdigest()

    # ===== LOAD =====
    def load_users(self):
        try:
            with open(self.data_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []

    # ===== SAVE =====
    def save_users(self, users):
        with open(self.data_path, "w", encoding="utf-8") as f:
            json.dump(users, f, indent=4, ensure_ascii=False)

    # ===== ADD USER =====
    def add_user(self, username, password, role):
        users = self.load_users()

        # check trùng username
        for u in users:
            if u["username"] == username:
                return False, "Username đã tồn tại"

        # tạo id mới
        new_id = max([u["id"] for u in users], default=0) + 1

        new_user = {
            "id": new_id,
            "username": username,
            "password": self.hash_pw(password),
            "role": role
        }

        users.append(new_user)
        self.save_users(users)

        return True, "Tạo user thành công"

    # ===== GET ALL =====
    def get_all_users(self):
        return self.load_users()

    # ===== DELETE =====
    def delete_user(self, user_id):
        users = self.load_users()
        new_users = [u for u in users if u["id"] != user_id]

        if len(new_users) == len(users):
            return False, "Không tìm thấy user"

        self.save_users(new_users)
        return True, "Xóa thành công"

    # ===== UPDATE =====
    def update_user(self, user_id, username, role):
        users = self.load_users()

        for u in users:
            if u["id"] == user_id:
                u["username"] = username
                u["role"] = role
                self.save_users(users)
                return True, "Cập nhật thành công"

        return False, "Không tìm thấy user"
    def ensure_admin(self):
        users = self.load_users()

        for u in users:
           if u["role"] == "ADMIN":
            return

        users.append({
            "id": 1,
        "username": "admin",
        "password": self.hash_pw("123456"),
        "role": "ADMIN"
    })

        self.save_users(users)