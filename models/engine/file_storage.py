#!/usr/bin/python3
"""File storage module for AirBnB clone."""
from models.base_model import BaseModel
import json
import os


class FileStorage:
    """
    Serializes instances to JSON file & deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds an object to __objects dictionary with key <obj class name>.id.
        """
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file (__file_path)."""
        obj_dict = {obj_id: obj.to_dict()
                    for obj_id, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes JSON file (__file_path) if __file_path exists.
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                objs = json.load(f)
                for obj_id, obj_dict in objs.items():
                    cls_name = obj_dict['__class__']
                    if cls_name == 'BaseModel':
                        self.new(BaseModel(**obj_dict))
