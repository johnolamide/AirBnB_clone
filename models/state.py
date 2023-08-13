#!/usr/bin/python3
""" Module contains the class definition of State
"""
from models.base_model import BaseModel


class State(BaseModel):
    """ State:
        Attributes:
            name (str):
    """
    name: str = ""
