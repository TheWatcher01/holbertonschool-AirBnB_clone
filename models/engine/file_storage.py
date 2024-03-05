#!/usr/bin/python3
"""This module contains file_storage for AirBnB clone"""
import models
import json
import os


class FileStorage:
    """Class serializes instances to a JSON file and deserializes JSON file
    to instances"""

    __file_path = "file.json"  # Path to JSON file
    __objects = {}  # Dictionary of objects

    def all(self):
        """Method returns dictionary __objects"""
        return FileStorage.__objects  # Return dictionary of objects

    def new(self, obj):
        """Method sets in __objects obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id  # Create key for object
        FileStorage.__objects[key] = obj  # Add object to dictionary

    def save(self):
        """Method serializes __objects to JSON file (path: __file_path)"""
        try:
            with open(FileStorage.__file_path, 'w') as file:  # Open file
                json.dump({key: obj.to_dict()  # Dump objects dict to file
                           for key, obj in FileStorage.__objects.items()}, file)
        except Exception as e:
            print(f"Error: {e}")

    def reload(self):
        """Method deserializes JSON file to __objects"""
        if os.path.exists(FileStorage.__file_path):  # If file exists
            try:
                with open(FileStorage.__file_path, 'r') as file:  # Open file
                    data = json.load(file)  # Load data from file
                    for key, value in data.items():  # For each item in data
                        class_name = value["__class__"]  # Get class name
                        value.pop("__class__", None)  # Remove __class__ key
                        cls = getattr(models, class_name)  # Get class
                        obj = cls(**value)  # Create a new object
                        FileStorage.__objects[key] = obj  # Add object to dict
            except Exception as e:
                print(f"Error: {e}")
        else:
            pass
