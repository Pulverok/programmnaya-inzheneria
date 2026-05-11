import unittest
from task import Task

class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task("Сделать домашку")
        self.assertEqual("Сделать домашку", task.get_title())

if __name__ == '__main__':
    unittest.main()
