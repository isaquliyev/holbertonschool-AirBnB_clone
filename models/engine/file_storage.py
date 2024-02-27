#!/usr/bin/python3

import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            f.write(json.dumps(new_dict))

    def reload(self):
        try:
            with open(self.__file_path, "r") as f:
                read_data = json.loads(f.read())
            for key in read_data:
                FileStorage.__objects[key] = BaseModel(**read_data[key])
        except Exception:
            pass
