import unittest
import pdb

from main import add, minus, sign_in, add_product


class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 5), 6)
        self.assertNotEqual(add(1, 5), 5)
        # self.assertEqual(add(1, 5), 5)

    def test_sign_in(self):
        self.assertTrue(sign_in("login", "password"))
        pdb.set_trace()
        self.assertFalse(sign_in("wrong_login", "password"))
        self.assertFalse(sign_in("login", "wrong_password"))
        self.assertFalse(sign_in("wrong_login", "wrong_password"))

    def test_add_product(self):
        self.assertEqual(add_product("login", "password", "product"), "product")
        self.assertIsNone(add_product("wrong_login", "password", "product"))


if __name__ == "__main__":
    unittest.main()