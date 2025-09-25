#!/usr/bin/python3
"""
Models package initialization
"""
from models.engine.file_storage import FileStorage
#!/usr/bin/python3
"""Models package"""
from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance
storage = FileStorage()
storage.reload()
storage = FileStorage()
storage.reload()