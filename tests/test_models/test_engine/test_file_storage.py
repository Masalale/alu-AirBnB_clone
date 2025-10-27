#!/usr/bin/python3
"""Unit tests for FileStorage class"""

import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    def setUp(self):
        """Set up test fixtures"""
        self.storage = FileStorage()
        # Clear the private class variable to ensure clean state
        FileStorage._FileStorage__objects = {}
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Clean up after tests"""
        FileStorage._FileStorage__objects = {}
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all_method(self):
        """Test all method returns objects dictionary"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_method(self):
        """Test new method adds object to storage"""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], obj)

    def test_save_method(self):
        """Test save method creates JSON file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

        with open("file.json", 'r') as f:
            data = json.load(f)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, data)

    def test_reload_method(self):
        """Test reload method loads objects from JSON file"""
        obj = BaseModel()
        self.storage.new(obj)
    self.storage.save()
        # Clear objects and reload
        self.storage._FileStorage__objects = {}
    self.storage.reload()

    key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())
        reloaded_obj = self.storage.all()[key]
        self.assertEqual(reloaded_obj.id, obj.id)
        self.assertIsInstance(reloaded_obj, BaseModel)

    def test_reload_no_file(self):
        """Test reload method when file doesn't exist"""
        # Should not raise an exception
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)

    def test_storage_with_different_classes(self):
        """Test storage works with all model classes"""
    classes = [BaseModel, User, Place, State, City, Amenity, Review]
        for cls in classes:
            obj = cls()
            self.storage.new(obj)
            key = f"{cls.__name__}.{obj.id}"
            self.assertIn(key, self.storage.all())
            self.assertIsInstance(self.storage.all()[key], cls)


if __name__ == '__main__':
    unittest.main()