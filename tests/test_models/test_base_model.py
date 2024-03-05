#!/usr/bin/python3
"""Unit tests for BaseModel."""
from models.base_model import BaseModel
from datetime import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    """Tests functionality of BaseModel class."""

    def setUp(self):
        """Setup for tests."""
        self.instance = BaseModel()

    def test_instance_creation(self):
        """Tests creation of an instance and its attributes."""
        self.assertTrue(hasattr(self.instance, "id"))
        self.assertTrue(hasattr(self.instance, "created_at"))
        self.assertTrue(hasattr(self.instance, "updated_at"))
        self.assertIsInstance(self.instance.id, str)
        self.assertIsInstance(self.instance.created_at, datetime)
        self.assertIsInstance(self.instance.updated_at, datetime)

    def test_id_uniqueness(self):
        """Tests uniqueness of IDs."""
        instance2 = BaseModel()
        self.assertNotEqual(self.instance.id, instance2.id)

    def test_datetime(self):
        """Tests created_at and updated_at attributes."""
        self.instance.save()
        self.assertNotEqual(self.instance.created_at, self.instance.updated_at)

    def test_to_dict(self):
        """Tests to_dict method."""
        model_dict = self.instance.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertEqual(model_dict['id'], self.instance.id)

    def test_from_dict(self):
        """Tests creation of an instance from a dictionary."""
        model_dict = self.instance.to_dict()
        instance2 = BaseModel(**model_dict)
        self.assertEqual(self.instance.id, instance2.id)
        self.assertEqual(self.instance.created_at, instance2.created_at)
        self.assertEqual(self.instance.updated_at, instance2.updated_at)

    def test_str_representation(self):
        """Tests __str__ method."""
        str_format = "[BaseModel] ({}) {}".format(
            self.instance.id, self.instance.__dict__)
        self.assertEqual(str(self.instance), str_format)


if __name__ == "__main__":
    unittest.main()
