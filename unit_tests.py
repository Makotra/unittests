import unittest
from main import rectangle  

class TestRectangle(unittest.TestCase):
    def test_correct_values(self):
        self.assertEqual(rectangle(5, 3), (1678000, 15))
        self.assertEqual(rectangle(7, 2), (18, 14))
    def test_negative_or_zero(self):
        with self.assertRaises(ValueError):
            rectangle(0, 5)
        with self.assertRaises(ValueError):
            rectangle(-3, 4)
    def test_edge_cases(self):
        self.assertEqual(rectangle(1, 1), (4, 1))

if __name__ == "__main__":
    unittest.main()