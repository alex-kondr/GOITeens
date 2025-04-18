import unittest


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)


    def test_subtract(self):
        self.assertEqual(subtract(10, 5), -5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)


    def test_subtract_raises(self):
        with self.assertRaises(TypeError):
            subtract("10", 5)


if __name__ == '__main__':
    unittest.main()