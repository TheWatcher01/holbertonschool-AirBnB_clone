#!/usr/bin/python3
"""Unittest for Place class"""


import unittest
from models import place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """
    Test the Place class
    """
    def setUp(self):
        """
        Set up an instance of Place
        """
        self.place = place.Place()

    def test_init(self):
        """
        Test if object is an instance of Place and BaseModel
        """
        # Test if object is an instance of Place
        self.assertIsInstance(self.place, place.Place)

        # Test if object is an instance of BaseModel
        self.assertIsInstance(self.place, BaseModel)

        # Test if attributes are set correctly
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_attr_types(self):
        """
        Test the attributes of Place
        """
        # Test type of attributes
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    def test_inheritance(self):
        """
        Test if Place is a subclass of BaseModel
        """
        # Test if Place is a subclass of BaseModel
        self.assertTrue(issubclass(place.Place, BaseModel))


if __name__ == '__main__':
    unittest.main()
