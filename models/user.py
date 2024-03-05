#!/usr/bin/python3
"""This module contains the User class for the AirBnB clone"""


from models import base_model


class User(base_model.BaseModel):
    """
    This class is a user for the AirBnB clone
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes the User"""
        super().__init__(*args, **kwargs)
