#!/usr/bin/python3
"""Unit tests for BaseModel class"""

import unittest
import os
import json
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def setUp(self):
        """Set up test fixtures"""
        storage._FileStorage__objects = {}
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Clean up after tests"""
        storage._FileStorage__objects = {}
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_init_without_kwargs(self):
        """Test BaseModel initialization without kwargs"""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        # created_at and updated_at should be very close but not necessarily equal
        time_diff = abs((model.created_at - model.updated_at).total_seconds())
        self.assertLess(time_diff, 1.0)  # Less than 1 second difference

    def test_init_with_kwargs(self):
        """Test BaseModel initialization with kwargs"""
        data = {
            'id': 'test-id',
            'created_at': '2023-01-01T12:00:00.000000',
            'updated_at': '2023-01-01T12:00:00.000000',
            'name': 'Test Model'
        }
        model = BaseModel(**data)
        self.assertEqual(model.id, 'test-id')
        self.assertEqual(model.name, 'Test Model')
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str_method(self):
        """Test string representation of BaseModel"""
        model = BaseModel()
        string = str(model)
        self.assertIn('[BaseModel]', string)
        self.assertIn(model.id, string)

    def test_save_method(self):
        """Test save method"""
        model = BaseModel()
        old_updated = model.updated_at
        model.save()
        self.assertNotEqual(old_updated, model.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method"""
        model = BaseModel()
        model.name = "Test"
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['name'], 'Test')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_unique_ids(self):
        """Test that different instances have unique ids"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)


if __name__ == '__main__':
    unittest.main()
