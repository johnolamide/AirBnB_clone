#!/usr/bin/python3
"""Definimg a new user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """This is the user class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
