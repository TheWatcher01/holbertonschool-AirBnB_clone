#!/usr/bin/python3
"""This module contains file_storage for AirBnB clone"""


import models
from models import base_model
from models import user
from models import state
from models import city
from models import amenity
from models import place
from models import review
import json
import os


classes = {
    "BaseModel": base_model.BaseModel,
    "User": user.User,
    "State": state.State,
    "City": city.City,
    "Amenity": amenity.Amenity,
    "Place": place.Place,
    "Review": review.Review
}

class FileStorage:
    """Class serializes instances to a JSON file and deserializes JSON file
    to instances"""

    __file_path = "file.json"  # Path to JSON file
    __objects = {}  # Dictionary of objects

    def all(self):
        """Method returns dictionary __objects"""
        return self.__objects  # Return dictionary of objects

    def new(self, obj):
        """Method sets in __objects obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id  # Create key for object
        self.__objects[key] = obj  # Add object to dictionary

    def save(self):
        """Method serializes __objects to JSON file (path: __file_path)"""
        try:
            objects_to_json = {}  # Create dictionary of objects
            for key in self.__objects: # For each key in __objects
                objects_to_json[key] = self.__objects[key].to_dict() # Add object to dict
            with open(self.__file_path, 'w') as file:  # Open file
                json.dump(objects_to_json, file)  # Write to file (serialize to JSON)
        except Exception as err:
            print(f"Error: {err}")

    def reload(self):
        """Method deserializes JSON file to __objects"""
        if os.path.exists(self.__file_path):  # If file exists
            try:
                with open(self.__file_path, 'r') as file:  # Open file
                    data = json.load(file)  # Load data from file
                    for key in data:  # For each item in data
                        class_name = data[key]["__class__"]  # Get class name
                        self.__objects[key] = classes[class_name](**data[key])  # Create new object
            except Exception as e:
                print(f"Error: {e}")
        else:
            pass
