#!/usr/bin/python3
"""Module contains BaseModel class for AirBnB clone"""
from datetime import datetime, timezone
from models import storage
import uuid


class BaseModel:
    """
    Defines all common attributes/methods for other classes.

    Attributes:
        id (str): Unique id for each BaseModel instance.
        created_at (datetime): The time when an instance is created.
        updated_at (datetime): The time when an instance is updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialization of BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Note:
            If kwargs is not empty, each key of this dict is attribute name.
            Each value of this dictionary is the value of this attribute name.
            If kwargs is empty, create id and created_at as new instance.

         Security Considerations:
            - Valid keys and values of kwargs before using them to prevent
              potential code injection
            - Handle ValueError that could occur when converting 'created_at'
              and 'updated_at' to datetime objects.
        """
        if kwargs:
            self.set_attributes(kwargs)
        else:
            self.create_new_instance()

    def set_attributes(self, kwargs):
        """
        Sets attributes from kwargs.

        Args:
            kwargs (dict): Arbitrary keyword arguments.

        Note:
            Each key of this dictionary is an attribute name.
            Each value of this dictionary is the value of this attribute name.

        Security Considerations:
            - Valid keys and values of kwargs before using them to prevent
              potential code injection
            - Handle ValueError that could occur when converting 'created_at'
              and 'updated_at' to datetime objects.

        Raises:
            ValueError: If 'created_at' or 'updated_at' cannot be converted to
            datetime object.
        """
        allowed_attrs = ['id', 'created_at', 'updated_at']
        for key, value in kwargs.items():
            if key in allowed_attrs:
                if key == 'created_at' or key == 'updated_at':
                    value = self.convert_to_datetime(value)
                setattr(self, key, value)

    def convert_to_datetime(self, value):
        """
        Converts a string to a datetime object.

        Args:
            value (str): The string to convert.

        Returns:
            datetime: The converted datetime object.

        Raises:
            ValueError: If 'value' cannot be converted to a datetime object.
        """
        try:
            value = value.replace("Z", "+00:00")
            return datetime.fromisoformat(value)
        except ValueError:
            raise ValueError(f"Cannot convert {value} to datetime object")

    def create_new_instance(self):
        """
        Creates a new instance with a unique id and the current time.

        Note:
            This method uses the 'storage' instance from the 'models' module.
        """
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now(timezone.utc)
        storage.new(self)

    def save(self):
        """
        Updates 'updated_at' attribute with current time and saves instance.

        Note:
            This method uses the 'storage' instance from the 'models' module.
        """
        self.updated_at = datetime.now(timezone.utc)
        storage.save()

    def to_dict(self):
        """
        Returns dictionary containing all keys/values of instance.

        Returns:
            dictionary: A new dictionary with all keys/values of the instance.
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def __str__(self):
        """
        Readable string representation of BaseModel instance.

        Returns:
            str: A string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
