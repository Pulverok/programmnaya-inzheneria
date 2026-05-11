class UserManager:
    """Модуль для управления пользователями."""
    def __init__(self, db):
        self.db = db

    def add_user(self, name):
        user = {"name": name, "type": "user"}
        self.db.save(user)
        return user
