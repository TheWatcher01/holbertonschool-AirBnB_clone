#!/usr/bin/python3
"""This module contains the file_storage for the AirBnB clone"""
import json
import os


class FileStorage:
    """Class serializes instances to a JSON file and deserializes JSON file
    to instances"""

    __file_path = "file.json"  # Path to the JSON file
    __objects = {}  # Dictionary of objects

    def all(self):
        """Method returns the dictionary __objects"""
        return FileStorage.__objects  # Return the dictionary of objects

    def new(self, obj):
        """Method sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id  # Create key for object
        FileStorage.__objects[key] = obj  # Add the object to the dictionary

    def save(self):
        """Method serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w') as file:  # Open the file
            # Dump the objects dictionary to the file
            json.dump({key: obj.to_dict()
                      for key, obj in FileStorage.__objects.items()}, file)

    def reload(self):
        """Method deserializes the JSON file to __objects"""
        if os.path.exists(FileStorage.__file_path):  # If the file exists
            with open(FileStorage.__file_path, 'r') as file:  # Open the file
                data = json.load(file)  # Load the data from the file
                for key, value in data.items():  # For each item in the data
                    class_name = value["__class__"]  # Get the class name
                    # Remove the class name from the value
                    value.pop("__class__", None)
                    obj = eval(class_name)(**value)  # Create a new object
                    # Add the object to the dictionary
                    FileStorage.__objects[key] = obj
