#!/usr/bin/python3
"""Test script to verify FileStorage serialization/deserialization"""

from models import storage
from models.base_model import BaseModel

# Test 1: Display reloaded objects
all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

# Test 2: Create a new object
print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)
