#!/usr/bin/python3
"""This module contains the Amenity class for the AirBnB clone"""


from models import base_model


class Amenity(base_model.BaseModel):
    """
    This class is an amenity for the AirBnB clone
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """initializes the Amenity"""
        super().__init__(*args, **kwargs)
