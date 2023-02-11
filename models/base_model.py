#!/usr/bin/python3
"""Module defines the base class"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Class defines the BaseModel that defines all
    common attributes for other classes"""
    def __init__(self):
        """Method takes care of the initialization,
        serialization/deserialization of future
        instances
        args:
        id: assigns an identity to an instance
        created_at: assigns with the current datetime
        when an instance is created.
        updated_at: assigns the current datetime an
        instance is created and is updated everytime
        the object is changed
	"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """returns a string representation of object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime
       	"""
        self.updated_at = datetime.now()
     
    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
