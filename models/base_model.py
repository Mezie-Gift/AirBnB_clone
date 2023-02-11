#!/usr/bin/python3
"""Module defines the base class"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Class defines the BaseModel that defines all
    common attributes for other classes"""
    def __init__(self, *args, **kwargs):
        """Method takes care of the initialization,
        serialization/deserialization of future
        instances
        args:
        *args: not used.
        **kwargs: any keyworded argument that may be
                  passed as parameter.
    """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """returns a string representation of object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
