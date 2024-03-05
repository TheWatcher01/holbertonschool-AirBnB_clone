import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """
    Test the functionality of the FileStorage class
    """
    def setUp(self):
        """Set up the tests"""
        self.storage = FileStorage()
        self.model = BaseModel()

    def test_all(self):
        """
        Test the all method of the FileStorage class
        """
        # Test if all returns a dictionary
        self.assertEqual(type(self.storage.all()), dict)

        # Test if all returns the correct dictionary
        self.storage.new(self.model)
        self.assertEqual(self.storage.all(), self.storage._FileStorage__objects)

    def test_new(self):
        """
        Test the new method of the FileStorage class
        """
        # Test if new adds an object to __objects
        self.storage.new(self.model)
        key = self.model.__class__.__name__ + "." + self.model.id
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """
        Test the save method of the FileStorage class
        """
        # Test if save creates a file
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

        # Test if save writes to a file
        with open(self.storage._FileStorage__file_path, 'r') as file:
            self.assertNotEqual(file.read(), "")

        # Test if save writes the correct data to a file
        with open(self.storage._FileStorage__file_path, 'r') as file:
            self.assertEqual(json.load(file), self.storage.all())

    def test_reload(self):
        """
        Test the reload method of the FileStorage class
        """
        # Test if reload reads from a file
        self.storage.reload()
        with open(self.storage._FileStorage__file_path, 'r') as file:
            self.assertEqual(json.load(file), self.storage.all())

        # Test if reload correctly updates __objects
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertNotEqual(self.storage.all(), {})

if __name__ == '__main__':
    unittest.main()