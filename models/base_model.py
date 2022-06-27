#!/usr/bin/python3
'''comentario'''


import models
import uuid
from datetime import datetime


class BaseModel():
    '''class Base'''
    def __init__(self):
        '''constructor class'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        '''string representation'''
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        '''update attribute updated_at with current datetime'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''return dict containing all key/value of __dict__ of an instance'''
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
