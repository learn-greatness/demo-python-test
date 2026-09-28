import unittest
from src.greetings import greet
class TestGreetings(unittest.TestCase):
    def test_greeting(self): self.assertEqual(greet("Alice"), "Hello, Alice!")
    def test_strips_whitespace(self): self.assertEqual(greet("  Alice  "), "Hello, Alice!")
