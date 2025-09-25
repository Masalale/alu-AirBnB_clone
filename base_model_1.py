#!/usr/bin/python3
"""Test file for BaseModel save method"""

from models.base_model import BaseModel

# Create a BaseModel instance
bm = BaseModel()

# Test the save method
bm.save()

# If we get here without errors, print OK
print("OK")