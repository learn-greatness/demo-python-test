import unittest
from src.counter import Counter
class TestCounter(unittest.TestCase):
    def test_starts_at_zero(self): self.assertEqual(Counter().value,0)
    def test_increment_and_decrement(self):
        c=Counter(); c.increment(); c.increment(); c.decrement(); self.assertEqual(c.value,1)
