#!/usr/bin/python3
"""
    This module contains our BaseModel class
"""

import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    This class defines all common attributes/
    methodes for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
            this is the __init__ fct ot initialize BaseModel attribute
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(
                                                        v,
                                                        "%Y-%m-%dT%H:%M:%S.%f"
                                    )
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """
            This fct save a new instance in our
            file.json

            Args:
                self: our instance
            Returns: Nothing
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """
            This fct return an string representation of an BaseModel instance
            Args:
                self: our instance
            Returns: an string representation of an BaseModel instance
        """
        return "[{}] ({}) {}".format(
                                    self.__class__.__name__,
                                    self.id,
                                    self.__dict__
                )

    def to_dict(self):
        """
            Return an dictionnary reprensentation of BaseModel Instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict["created_at"] = self.created_at.isoformat()
        return obj_dict
