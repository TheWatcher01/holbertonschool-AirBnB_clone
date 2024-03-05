#!/usr/bin/python3
"""Module contains BaseModel class for AirBnB clone"""


import models
from datetime import datetime
import uuid


format_style = '%Y-%m-%dT%H:%M:%S.%f'


class BaseModel:
    """This class is base model for all other classes in this project"""

    def __init__(self, *args, **kwargs):
        """
        Method initializes new instance of BaseModel class
        Args:
            args: Unused, for future use
            kwargs: Dictionary of key/value pairs
        """
        if kwargs:  # If kwargs is not empty
            for key, value in kwargs.items():
                # If key is created_at or updated_at...
                if key in ["created_at", "updated_at"]:
                    # ...Convert value to datetime object
                    setattr(self, key, datetime.strptime(value, format_style))
                # If key is not __class__...
                elif key != "__class__":
                    # ...Set attribute of instance to key/value
                    setattr(self, key, value)
        else:  # If kwargs is empty, initialize with default values
            self.id = str(uuid.uuid4())  # Set id to random UUID
            # Set created_at to current time
            self.created_at = datetime.utcnow()
            # Set updated_at to current time
            self.updated_at = datetime.utcnow()
        models.storage.new(self)  # Add new instance to FileStorage.__objects

    def __str__(self):
        """Method returns string representation of BaseModel instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Method updates updated_at attribute with current time"""
        self.updated_at = datetime.now()
        # Save to file without importing FileStorage
        models.storage.save()

    def to_dict(self):
        """Method to dictionary containing all keys/values  of __dict__
        of BaseModel instance

        Returns:
            dict: Of instance's __dict__ with 'created_at' and 'updated_at'
            in ISO format, and includes '__class__' key.
        """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
