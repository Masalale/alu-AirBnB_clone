#!/usr/bin/python3
"""FileStorage module for AirBnB clone project"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """FileStorage class for serializing/deserializing instances to/from JSON"""
#!/usr/bin/python3
"""FileStorage module"""
import json
import os


class FileStorage:
    """FileStorage class for serialization and deserialization"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)

            for key, value in obj_dict.items():
                class_name = value['__class__']
                if class_name == 'BaseModel':
                    from models.base_model import BaseModel
                    FileStorage.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file"""
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()
        
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize the JSON file to __objects"""
        classes = {
            'BaseModel': BaseModel,
            'User': User,
            'Place': Place,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Review': Review
        }

        if os.path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                    obj_dict = json.load(f)
                
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    if class_name in classes:
                        FileStorage.__objects[key] = classes[class_name](**value)
            except (FileNotFoundError, json.JSONDecodeError):
                pass
