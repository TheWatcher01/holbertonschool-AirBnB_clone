#!/usr/bin/python3
"""This module contains Place class for the AirBnB clone"""


from models import base_model


class Place(base_model.BaseModel):
    """
    This class is a place for the AirBnB clone
    Note: Place class is empty for now to work with FileStorage
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initializes the Place"""
        super().__init__(*args, **kwargs)
