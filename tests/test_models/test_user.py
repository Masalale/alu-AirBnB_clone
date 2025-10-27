#!/usr/bin/python3
"""Unit tests for User class"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for User class"""

    def test_inheritance(self):
        """Test User inherits from BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_attributes(self):
        """Test User has required attributes"""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_attribute_assignment(self):
        """Test User attribute assignment"""
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
    user.last_name = "Doe"

        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_to_dict(self):
        """Test User to_dict method"""
        user = User()
        user.email = "test@example.com"
        user_dict = user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], 'test@example.com')


if __name__ == '__main__':
    unittest.main()
