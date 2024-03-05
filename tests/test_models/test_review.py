#!/usr/bin/python3
"""Unittest for Review class"""


import unittest
from models import review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """
    Test the Review class
    """
    def setUp(self):
        """
        Set up an instance of Review
        """
        self.review = review.Review()

    def test_init(self):
        """
        Test if object is an instance of Review and BaseModel
        """
        # Test if object is an instance of Review
        self.assertIsInstance(self.review, review.Review)

        # Test if object is an instance of BaseModel
        self.assertIsInstance(self.review, BaseModel)

        # Test if attributes are set correctly
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_attr_types(self):
        """
        Test the attributes of Review
        """
        # Test type of attributes
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.user_id), str)
        self.assertEqual(type(self.review.text), str)

    def test_inheritance(self):
        """
        Test if Review is a subclass of BaseModel
        """
        # Test if Review is a subclass of BaseModel
        self.assertTrue(issubclass(review.Review, BaseModel))


if __name__ == '__main__':
    unittest.main()
