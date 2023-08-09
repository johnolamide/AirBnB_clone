#!/usr/bin/python3
""" Module contains the class definition of BaseModel
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
        BaseModel:
        Attributes:
            id (string):
            created_at (datetime):
            updated_at (datetime):
        methods:
            __init__: initialize a BaseModel instance
            __str__: string representation of the BaseModel Object
            save: Updates the Object Instance
            to_dict: Returns a dictionary representation of an Instance
    """

    def __init__(self, *args, **kwargs):
        """ Create a BaseModel Object from kwargs
            or initialize the instance variable
            Args:
                *args: None
                **kwargs (dict): key-value pairs for instance creation
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
            storage.new(self)

    def __str__(self):
        """ String representation of the BaseModel Object
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ Updates self.updated_at to current time
            and saves the changes in the storage object
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns the dictionary representation of the
            BaseModel Object
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
