import unittest
from src.users import find_user_by_id
class TestUsers(unittest.TestCase):
    def test_finds_user(self):
        users=[{"id":1,"name":"Alice"},{"id":2,"name":"Bob"}]
        self.assertEqual(find_user_by_id(users,2), {"id":2,"name":"Bob"})
    def test_missing_user(self): self.assertIsNone(find_user_by_id([{"id":1,"name":"Alice"}],99))
