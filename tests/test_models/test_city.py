#!/usr/bin/python3
"""Unittest for city"""


import unittest
from models import city
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    Test the City class
    """
    def setUp(self):
        """
        Set up an instance of City
        """
        self.city = city.City()

    def test_init(self):
        """
        Test if object is an instance of City and BaseModel
        """
        # Test if object is an instance of City
        self.assertIsInstance(self.city, city.City)

        # Test if object is an instance of BaseModel
        self.assertIsInstance(self.city, BaseModel)

        # Test if name and state_id are empty strings
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")

    def test_attr_types(self):
        """
        Test the attributes of City
        """
        # Test type of name and state_id
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_inheritance(self):
        """
        Test if City is a subclass of BaseModel
        """
        # Test if City is a subclass of BaseModel
        self.assertTrue(issubclass(city.City, BaseModel))


if __name__ == '__main__':
    unittest.main()
