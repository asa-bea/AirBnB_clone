#!/usr/bin/python3

"""
A module that contains the BaseModel class
"""

import uuid
from datetime import datetime
import models


class BaseModel():
    """
    This is BaseModel which will serve as the parent of all other model class
    """

    def __init__(self, *args, **kwargs):
        """Instance Attribute Initialization"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs):
            for key, value in kwargs.items():
                if key == "__class__":
                    continue

                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                    continue

                setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        """ controls what the various instances should return """

        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates the updated_at attribute of the instance """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all key/values of that instances """

        instance_dict = self.__dict__.copy()
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        instance_dict["__class__"] = self.__class__.__name__

        return (instance_dict)
