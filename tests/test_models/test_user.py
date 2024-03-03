#!/usr/bin/python3

import os
import unittest

from models import storage
from models.user import User


class TestUser(unittest.TestCase):
    """
    unit tests for the User class.
    """

    def setUp(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_email_type(self):
        user_model = User()
        self.assertIsInstance(user_model.email, str)

    def test_password_type(self):
        user_model = User()
        self.assertIsInstance(user_model.password, str)

    def test_first_name_type(self):
        user_model = User()
        self.assertIsInstance(user_model.first_name, str)

    def test_last_name_type(self):
        user_model = User()
        self.assertIsInstance(user_model.last_name, str)

    def test_email(self):
        user_model = User()
        user_model.email = "test@gmail.com"
        self.assertEqual(user_model.email, "test@gmail.com")

    def test_password(self):
        user_model = User()
        user_model.password = "test"
        self.assertEqual(user_model.password, "test")

    def test_first_name(self):
        user_model = User()
        user_model.first_name = "Test"
        self.assertEqual(user_model.first_name, "Test")

    def test_last_name(self):
        user_model = User()
        user_model.last_name = "Test"
        self.assertEqual(user_model.last_name, "Test")

if __name__ == '__main__':
    unittest.main()

