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


class FileStorage:
    """Class serializes instances to a JSON file and deserializes JSON file
    to instances"""

    __classes = {
        "BaseModel": base_model.BaseModel,
        "User": user.User,
        "State": state.State,
        "City": city.City,
        "Amenity": amenity.Amenity,
        "Place": place.Place,
        "Review": review.Review
    }
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
            with open(self.__file_path, 'r') as file:  # Open file
                data = json.load(file)  # Load data from file
                for key in data:  # For each item in data
                    class_name = data[key]["__class__"]  # Get class name
                    if class_name in self.__classes:
                        # Create new object
                        self.__objects[key] = self.__classes[class_name](**data[key])
        except FileNotFoundError:
            # If file not found (first time program runs)
            pass

    def class_exists(self, class_name: str):
        """Method checks if class exists"""
        return class_name in self.__classes

    def get_class(self, class_name: str):
        """Method returns class"""
        return self.__classes.get(class_name)

    def get(self, class_name: str, id: str) -> base_model.BaseModel:
        """Method retrieves an object based on class name and id"""
        key = class_name + "." + id
        return self.__objects.get(key)

    def delete(self, obj=None):
        """Method deletes obj from __objects if it’s inside"""
        if obj:
            key = obj.__class__.__name__ + "." + obj.id
            if key in self.__objects:
                del self.__objects[key]
            self.save()
