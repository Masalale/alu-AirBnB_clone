#!/usr/bin/python3
"""FileStorage module for the AirBnB clone project.

This module defines the FileStorage class which serializes and
deserializes instances to and from a JSON file.
"""

from __future__ import annotations

import json
import os
from typing import Dict

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file and deserializes back.

    Attributes:
        __file_path (str): path to the JSON file.
        __objects (dict): in-memory storage of objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self) -> Dict[str, object]:
        """Return the dictionary of stored objects."""
        return FileStorage.__objects

    def new(self, obj: object) -> None:
        """Add an object to the storage dictionary.

        The key format is <class name>.<id>.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self) -> None:
        """Serialize __objects to the JSON file."""
        obj_dict = {
            key: obj.to_dict()
            for key, obj in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self) -> None:
        """Deserialize the JSON file to __objects if the file exists."""
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
        }

        if not os.path.exists(FileStorage.__file_path):
            return

        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)

            for key, value in obj_dict.items():
                class_name = value.get("__class__")
                if class_name in classes:
                    FileStorage.__objects[key] = classes[
                        class_name](**value)
        except (FileNotFoundError, json.JSONDecodeError):
            # If file is missing or corrupted, skip reloading.
            pass
