#!/usr/bin/python3
"""This module contains the State class for the AirBnB clone"""


from models import base_model


class State(base_model.BaseModel):
    """
    This class is a state for the AirBnB clone
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """initializes the State"""
        super().__init__(*args, **kwargs)
