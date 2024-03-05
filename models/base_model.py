#!/usr/bin/python3
"""Module contains BaseModel class for AirBnB clone"""
from models.engine.file_storage import FileStorage
from datetime import datetime
import uuid


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
                    setattr(self, key, datetime.fromisoformat(value))
                # If key is not __class__...
                elif key != "__class__":
                    # ...Set attribute of instance to key/value
                    setattr(self, key, value)
        else:  # If kwargs is empty, initialize with default values
            self.id = str(uuid.uuid4())  # Set id to random UUID
            self.created_at = datetime.now()  # Set created_at to current time
            self.updated_at = datetime.now()  # Set updated_at to current time

    def __str__(self):
        """Method returns string representation of BaseModel instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Method updates updated_at attribute with current time"""
        self.updated_at = datetime.now()
        FileStorage().save()

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
