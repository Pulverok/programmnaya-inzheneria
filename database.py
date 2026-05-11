class Database:
    """Модуль для работы с базой данных."""
    def __init__(self):
        self.data = []

    def save(self, item):
        self.data.append(item)

    def get_all(self):
        return self.data
