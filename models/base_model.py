#!/usr/bin/python3
"""This module contains the BaseModel class for the AirBnB clone"""

import uuid
from datetime import datetime


class BaseModel:
    """This class is the base model for all other classes in this project"""
    def __init__(self, *args, **kwargs):
        """This method initializes a new instance of the BaseModel class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
    def save(self):
        """This method updates the updated_at attribute with the current time"""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """Method returns a dictionary containing all keys/values  of __dict__ of the BaseModel instance"""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
    
    def __str__(self):
        """This method returns a string representation of the BaseModel instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.to_dict()}"
