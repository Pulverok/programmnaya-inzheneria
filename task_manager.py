from dataclasses import dataclass

@dataclass
class Task:
    """Структура данных для задачи."""
    name: str
    priority: str
    type: str = "task"

class TaskManager:
    """Модуль управления задачами."""
    
    def __init__(self, db):
        self.db = db

    def create_task(self, name: str, priority: str) -> Task:
        """Создает новую задачу."""
        task = Task(name=name, priority=priority)
        self.db.save(task)
        return task

    def update_task(self, task: Task, new_name: str, new_priority: str) -> Task:
        """Обновляет существующую задачу."""
        task.name = new_name
        task.priority = new_priority
        return task

    def get_all_tasks(self):
        return [item for item in self.db.get_all() if getattr(item, 'type', None) == "task"]
