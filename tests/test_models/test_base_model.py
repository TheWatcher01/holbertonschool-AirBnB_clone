#!/usr/bin/python3
""" Unittest for BaseModel """
from models.base_model import BaseModel
from datetime import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    """Test the functionality of the BaseModel class"""
    def setUp(self):
        """Set up the tests"""
        self.model = BaseModel()

    def test_id(self):
        """Test the id attribute of the BaseModel class"""
        self.assertIsInstance(self.model.id, str)

    def test_created_at(self):
        """Test the created_at attribute of the BaseModel class"""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at(self):
        """Test the updated_at attribute of the BaseModel class"""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save(self):
        """Test the save method of the BaseModel class"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test the to_dict method of the BaseModel class"""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertEqual(model_dict["created_at"],
                         self.model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"],
                         self.model.updated_at.isoformat())

    def test_str(self):
        """Test the __str__ method of the BaseModel class"""
        model_str = self.model.__str__()
        expected_str = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(model_str, expected_str)


if __name__ == '__main__':
    unittest.main()
