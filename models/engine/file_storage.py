#!/usr/bin/python3
""" Module contains the class definition for the FileStorage Class
"""
import json
#from models import models


class FileStorage:
    #from models import models
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
        FileStorage.__objects[key] = obj

    def save(self):
        """ Write contents of FileStorage.__objects
            to a json file in FileStorage.__file_path
        """
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """ Read contents from FileStorage.__file_path
            to FileStorage.__objects
        """
        from models import models
        obj_dict = {}
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    className = value["__class__"]
                    if className in models:
                        obj = models[className](**value)
                        FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
#    def reload(self):
#        from models import models
#        obj_dict = {}
#        try:
#            with open(FileStorage.__file_path, 'r') as file:
#                obj_dict = json.load(file)
#                for key, value in obj_dict.items():
#                    className = value["__class__"]
#                    if className in models:
#                        print("key: {}. className: {}".format(key, className))
#                FileStorage.__objects = obj_dict
#        except FileNotFoundError:
#            pass
