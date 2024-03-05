#!/usr/bin/python3
"""This module contains the Review class for the AirBnB clone"""


from models import base_model


class Review(base_model.BaseModel):
    """
    This class is a review for the AirBnB clone
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes the Review"""
        super().__init__(*args, **kwargs)
