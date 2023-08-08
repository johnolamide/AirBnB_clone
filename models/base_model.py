#!/usr/bin/python3
""" Module contains the class definition of BaseModel
"""
import uuid
from datetime import datetime


class BaseModel:
    """
        BaseModel:
        Attributes:
            id (string):
            created_at (datetime):
            updated_at (datetime):
        methods:
            __init__:
            __str__:
            save:
            to_dict:
    """

    def __init__(self, *args, **kwargs):
        """
        """
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, date_format)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
