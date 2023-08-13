#!/usr/bin/python3
""" Module contains the class definition of Amenity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity:
        Attributes:
            name (str):
    """
    name: str = ""
