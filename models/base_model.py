#!/usr/bin/python3
"""Module contains BaseModel class for AirBnB clone"""
from datetime import datetime
import models
import uuid


class BaseModel:
    """Defines all common attributes for various models."""

    def __init__(self, *args, **kwargs):
        """Initialization of BaseModel class."""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Updates 'updated_at' attribute with current time."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns dictionary containing all keys/values of instance."""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def __str__(self):
        """Returns readable representation of BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
