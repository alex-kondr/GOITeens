import unittest
from unittest.mock import patch, MagicMock
import json
import os

from users import get_users, save_users, sign_up, login_user


# file_path = "test_users_db.json"
mock = MagicMock(return_value=[])


class TestUser(unittest.TestCase):
    # def setUp(self):
    #     with open(file_path, "w") as file:
    #         json.dump([], file)

    # def tearDown(self):
    #     os.remove(file_path)

    # @patch("users.save_users", lambda users: save_users(users, file_path))
    # @patch("users.get_users", lambda: get_users(file_path))
    @patch("users.get_users", MagicMock())
    @patch("users.save_users", MagicMock())
    def test_sign_up(self):
        self.assertTrue(sign_up("login", "password", "name"))

    # @patch("users.save_users", lambda users: save_users(users, file_path))
    # @patch("users.get_users", lambda: get_users(file_path))
    @patch("users.get_users", mock)
    @patch("users.save_users", mock)
    def test_login_user(self):
        self.assertTrue(sign_up("login", "password", "name"))
        self.assertIsNotNone(login_user("login", "password"))
        self.assertRaises(ValueError, login_user, "wrong_login", "password")
        self.assertRaises(ValueError, login_user, "login", "wrond_password")
        self.assertRaises(ValueError, login_user, "wrong_login", "wrond_password")


if __name__ == "__main__":
    unittest.main()
