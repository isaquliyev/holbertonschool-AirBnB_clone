#!/usr/bin/python3
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()

class_list = ["BaseModel",
              "User",
              "City",
              "Place",
              "State",
              "Amenity",
              "Review"]
