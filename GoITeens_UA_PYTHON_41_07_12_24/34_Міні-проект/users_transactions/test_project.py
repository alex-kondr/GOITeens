import unittest
from unittest.mock import patch
import os
import json

from users import save_users, sign_up, get_users, login_user


def mock_save_users(users, file: str = "mock_users_db.json"):
    save_users(users, file)


def mock_get_users(file: str = "mock_users_db.json"):
    return get_users(file)


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        with open("mock_users_db.json", "w", encoding="utf-8") as fd:
            json.dump([], fd, ensure_ascii=False, indent=2)

    def tearDown(self):
        os.remove("mock_users_db.json")

    @patch("users.save_users", mock_save_users)
    @patch("users.get_users", mock_get_users)
    def test_sign_up(self):
        self.assertTrue(sign_up("login", "password", "name"))

    @patch("users.save_users", mock_save_users)
    @patch("users.get_users", mock_get_users)
    def test_login_user(self):
        sign_up("login", "password", "name")
        self.assertIsNotNone(login_user("login", "password"))
        self.assertRaises(ValueError, login_user, "login", "wrong_password")
        self.assertRaises(ValueError, login_user, "wrong_login", "password")
        self.assertRaises(ValueError, login_user, "wrong_login", "wrong_password")


if __name__ == '__main__':
    unittest.main()
