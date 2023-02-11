#!/usr/bin/python3
"""Module defines a FileStorage class"""
import json
from models import base_model


class FileStorage:
    """serializes instances to a JSON file and
    deserializes JSON file to instances
    args:
     __file_path:string - path to the JSON file
     __objects:dictionary - empty but will store all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            d = {key: value.to_dict() for key, value in self.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path)
        exists otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                python_dict = json.load(f)
                for obj_v in python_dict.values():
                    cls_name = obj_v["__class__"]
                    del obj_v["__class__"]
                    self.new(eval(f"base_model.{cls_name}")(**obj_v))
        except FileNotFoundError:
            return
