#!/usr/bin/python3
"""Unittest for User class"""


import unittest
from models import user
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    Test the User class
    """
    def setUp(self):
        """
        Set up an instance of User
        """
        self.user = user.User()

    def test_init(self):
        """
        Test if object is an instance of User and BaseModel
        """
        # Test if object is an instance of User
        self.assertIsInstance(self.user, user.User)

        # Test if object is an instance of BaseModel
        self.assertIsInstance(self.user, BaseModel)

        # Test if email, password, first_name, last_name are empty strings
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_attr_types(self):
        """
        Test the attributes of User
        """
        # Test type of email, password, first_name, last_name
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.last_name), str)

    def test_inheritance(self):
        """
        Test if User is a subclass of BaseModel
        """
        # Test if User is a subclass of BaseModel
        self.assertTrue(issubclass(user.User, BaseModel))
