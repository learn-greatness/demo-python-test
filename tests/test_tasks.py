import unittest
from src.tasks import add_task, complete_task
class TestTasks(unittest.TestCase):
    def test_add_task(self):
        tasks=[]; task=add_task(tasks,"Learn Python")
        self.assertEqual(task["id"],1); self.assertEqual(task["title"],"Learn Python"); self.assertFalse(task["completed"])
    def test_complete_task(self):
        tasks=[]; add_task(tasks,"Learn Python"); task=complete_task(tasks,1); self.assertTrue(task["completed"])
