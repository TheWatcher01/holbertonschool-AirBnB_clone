#!/usr/bin/python3
"""This module contains the State class for the AirBnB clone"""


from models import base_model


class City(base_model.BaseModel):
    """
    This class is a city for the AirBnB clone
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes the City"""
        super().__init__(*args, **kwargs)
