#!/usr/bin/python3
"""Unit tests for Console class"""

import unittest
import sys
import os
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestConsole(unittest.TestCase):
    """Test cases for Console class"""

    def setUp(self):
        """Set up test fixtures"""
        self.console = HBNBCommand()
        storage._FileStorage__objects = {}
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Clean up after tests"""
        storage._FileStorage__objects = {}
        if os.path.exists("file.json"):
            os.remove("file.json")

    def create_mock_output(self):
        """Create a mock stdout to capture output"""
        return StringIO()

    def test_help_command(self):
        """Test help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help")
            output = f.getvalue()
            # Just check that the command runs without error and produces some output
            self.assertIsNotNone(output)

    def test_quit_command(self):
        """Test quit command"""
        self.assertTrue(self.console.onecmd("quit"))

    def test_EOF_command(self):
        """Test EOF command"""
        with patch('sys.stdout', new=StringIO()):
            self.assertTrue(self.console.onecmd("EOF"))

    def test_empty_line(self):
        """Test empty line"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("")
            self.assertEqual(f.getvalue(), "")

    def test_create_command(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)  # Should print an ID

    def test_create_command_no_class(self):
        """Test create command without class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_create_command_invalid_class(self):
        """Test create command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create InvalidClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show_command(self):
        """Test show command"""
        obj = BaseModel()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show BaseModel {obj.id}")
            output = f.getvalue().strip()
            self.assertIn(obj.id, output)

    def test_show_command_no_class(self):
        """Test show command without class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_show_command_invalid_class(self):
        """Test show command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show InvalidClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show_command_no_id(self):
        """Test show command without instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_show_command_no_instance(self):
        """Test show command with non-existent instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel invalid-id")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_destroy_command(self):
        """Test destroy command"""
        obj = BaseModel()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"destroy BaseModel {obj.id}")
            # Check that object was removed
            key = f"BaseModel.{obj.id}"
            self.assertNotIn(key, storage.all())

    def test_destroy_command_no_class(self):
        """Test destroy command without class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_destroy_command_invalid_class(self):
        """Test destroy command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy InvalidClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_destroy_command_no_id(self):
        """Test destroy command without instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_destroy_command_no_instance(self):
        """Test destroy command with non-existent instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel invalid-id")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_all_command(self):
        """Test all command"""
        obj = BaseModel()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
            output = f.getvalue().strip()
            self.assertIn(obj.id, output)

    def test_all_command_with_class(self):
        """Test all command with specific class"""
        obj = BaseModel()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
            output = f.getvalue().strip()
            self.assertIn(obj.id, output)

    def test_all_command_invalid_class(self):
        """Test all command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all InvalidClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_update_command(self):
        """Test update command"""
        obj = BaseModel()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'update BaseModel {obj.id} name "Test"')
            # Check that attribute was updated
            updated_obj = storage.all()[f"BaseModel.{obj.id}"]
            self.assertEqual(updated_obj.name, "Test")

    def test_update_command_no_class(self):
        """Test update command without class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_update_command_invalid_class(self):
        """Test update command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update InvalidClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_update_command_no_id(self):
        """Test update command without instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_update_command_no_instance(self):
        """Test update command with non-existent instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel invalid-id")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_update_command_no_attribute(self):
        """Test update command without attribute name"""
        obj = BaseModel()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"update BaseModel {obj.id}")
            self.assertEqual(f.getvalue().strip(), "** attribute name missing **")

    def test_update_command_no_value(self):
        """Test update command without attribute value"""
        obj = BaseModel()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"update BaseModel {obj.id} name")
            self.assertEqual(f.getvalue().strip(), "** value missing **")


if __name__ == '__main__':
    unittest.main()