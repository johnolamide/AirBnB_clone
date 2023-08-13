#!/usr/bin/python3
""" Module contains the class definition for User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ User:
        Attributes:
            email (str):
            password (str):
            first_name (str):
            last_name (str):
    """
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
