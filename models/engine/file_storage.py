#!/usr/bin/python3
""" Module contains the class definition for the FileStorage Class
"""
import json


class FileStorage:
    """
        FileStorage:
        Attributes:
            __file_path (string):
            __objects (dict):
        Methods:
            __init__(self):
            all(self): returns the contents of the __objects class attribute
            new(self, obj): adds a new obj instance to the __objects attribute
            save(self): write content of __objects to __file_path
            reload(self): read content from __file_path to __objects
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """
        """

    def all(self):
        """ Returns the content of the FileStorage.__objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """ Adds a new obj instance to FileStorage.__objects
            Args:
                obj: object
        """
        className = obj.__class__.__name__
        objectId = obj.id
        key = "{}.{}".format(className, objectId)
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """ Write contents of FileStorage.__objects
            to a json file in FileStorage.__file_path
        """
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        """ Read contents from FileStorage.__file_path
            to FileStorage.__objects
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                FileStorage.__objects = json.load(file)
        except FileNotFoundError:
            pass
