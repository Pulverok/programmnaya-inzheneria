class UserManager:
    """Модуль для управления пользователями."""
    def __init__(self, db):
        self.db = db

    def add_user(self, name):
        user = {"name": name, "type": "user"}
        self.db.save(user)
        return user

    def authenticate_user(self, email, password):
        """Авторизация пользователя через email."""
        # Мок авторизации
        print(f"Пользователь {email} успешно авторизован.")
        return True
