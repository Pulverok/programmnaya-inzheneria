class TaskManager:
    """Модуль управления задачами."""
    
    def __init__(self, db):
        self.db = db

    def modify_task(self, task=None, name="", priority=""):
        """Создает или обновляет задачу (устранение дублирования кода)."""
        if task is None:
            new_task = {"name": name, "priority": priority, "type": "task"}
            self.db.save(new_task)
            return new_task
        
        task["name"] = name
        task["priority"] = priority
        return task

    def get_all_tasks(self):
        return [item for item in self.db.get_all() if item.get("type") == "task"]
