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
            for key in self.__objects:  # For each key in __objects
                # Add object to dictionary
                objects_to_json[key] = self.__objects[key].to_dict()
            with open(self.__file_path, 'w') as file:  # Open file
                # Write to file (serialize to JSON)
                json.dump(objects_to_json, file)
        except Exception as err:
            print(f"Error: {err}")

    def reload(self):
        """Method deserializes JSON file to __objects"""
        try:
            try:
                with open(self.__file_path, 'r') as file:  # Open file
                    data = json.load(file)  # Load data from file
                    for key in data:  # For each item in data
                        class_name = data[key]["__class__"]  # Get class name
                        # Create new object
                        self.__objects[key] = classes[class_name](**data[key])
            except Exception as e:
                print(f"Error: {e}")
        except FileNotFoundError:
            # If file not found (first time program runs)
            pass
