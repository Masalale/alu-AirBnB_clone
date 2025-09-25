#!/usr/bin/python3
"""Unit tests for Review class"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def test_inheritance(self):
        """Test Review inherits from BaseModel"""
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_attributes(self):
        """Test Review has required attributes"""
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_attribute_assignment(self):
        """Test Review attribute assignment"""
        review = Review()
        review.place_id = "place-123"
        review.user_id = "user-456"
        review.text = "Great place!"
        self.assertEqual(review.place_id, "place-123")
        self.assertEqual(review.user_id, "user-456")
        self.assertEqual(review.text, "Great place!")

    def test_to_dict(self):
        """Test Review to_dict method"""
        review = Review()
        review.text = "Great place!"
        review_dict = review.to_dict()
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['text'], 'Great place!')


if __name__ == '__main__':
    unittest.main()