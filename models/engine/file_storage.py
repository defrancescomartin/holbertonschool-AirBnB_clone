#!/usr/bin/python3
'''Write a class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances
'''

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    '''creating class'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''return a dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''sets in obj the obj with key'''
        obj_name = (f"{obj.__class__.__name__}.{obj.id}")
        self.__objects[obj_name] = obj

    def save(self):
        '''serialize __obj to the json file'''
        new_dic = {}
        for key, value in self.__objects.items():
            new_dic[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(new_dic, f)

    def reload(self):
        '''deserialize json file to __obj'''
        if os.path.isfile(self.__file_path) is False:
            return
        else:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                dic = json.load(f)
            for key, value in dic.items():
                self.__objects[key] = eval(value["__class__"])(**value)
