import unittest
from src.cart import calculate_total
class TestCart(unittest.TestCase):
    def test_calculates_total(self):
        self.assertEqual(calculate_total([{"name":"Book","price":100,"quantity":2},{"name":"Pen","price":20,"quantity":3}]), 260)
    def test_empty_cart(self): self.assertEqual(calculate_total([]), 0)
