#!/usr/bin/python3
'''
Previously we created a method to generate a dictionary representation of an
instance (method to_dict()).
Now it’s time to re-create an instance with this dictionary representation.
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
'''


import models
import uuid
from datetime import datetime
from models import storage

class BaseModel():
    '''class Base'''
    def __init__(self, *args, **kwargs):
        '''constructor class'''

        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.now()
                else:
                    self.__dict__[key] = value
        
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new()

    def __str__(self):
        '''string representation'''
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        '''update attribute updated_at with current datetime'''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''return dict containing all key/value of __dict__ of an instance'''
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["created_at"] = self.created_at.isoformat()
        return dictionary
