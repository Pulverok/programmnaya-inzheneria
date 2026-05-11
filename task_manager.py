class TaskManager:
    """Класс для управления задачами."""

    MAX_TASKS = 100

    def __init__(self):
        self.tasks = []

    def add(self, task):
        if len(self.tasks) < self.MAX_TASKS:
            self.tasks.append(task)
        else:
            print('too many')

    def get_all(self):
        return self.tasks
