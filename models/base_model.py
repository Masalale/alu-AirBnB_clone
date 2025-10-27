#!/usr/bin/python3
"""BaseModel module for AirBnB clone project"""

import uuid
from datetime import datetime


class BaseModel:
    """Base class for all models in AirBnB clone"""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            import models
            models.storage.new(self)

    def __str__(self):
        """String representation of BaseModel"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates updated_at and saves to storage"""
        self.updated_at = datetime.now()
        import models
        models.storage.save()
        return "OK"

    def to_dict(self):
        """Returns dictionary representation of BaseModel."""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
