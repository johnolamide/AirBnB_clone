#!/usr/bin/python3
""" Module contains the class definition of Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review:
        Attributes:
            place_id (str):
            user_id (str):
            text (str):
    """
    place_id: str = ""
    user_id: str = ""
    text: str = ""
