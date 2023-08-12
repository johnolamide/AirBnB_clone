#!/usr/bin/python3
""" Module contains the class definition of City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ City:
        Attributes:
            state_id (str):
            name (str):
    """
    state_id: str = ""
    name: str = ""
