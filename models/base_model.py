#!/usr/bin/python3
"""Module contains BaseModel class for AirBnB clone"""
import uuid
from datetime import datetime


class BaseModel:
    """This class is base model for all other classes in this project"""
    def __init__(self, *args, **kwargs):
        """Method initializes new instance of BaseModel class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Method updates updated_at attribute with current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Method returns dictionary containing all keys/values  of __dict__
        of BaseModel instance"""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy

    def __str__(self):
        """Method returns string representation of BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.to_dict())
