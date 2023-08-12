#!/usr/bin/python3
""" Module contains the class definition of Place
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ Place:
        Attributes:
            city_id (str):
            user_id (str):
            name (str):
            description (str):
            number_rooms (int):
            number_bathrooms (int):
            max_guest (int):
            price_by_night (int):
            latitude (float):
            longitude (float):
            amenity_id (list):
    """
    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_id: list = []
