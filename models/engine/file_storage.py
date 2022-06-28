#!/usr/bin/python3
'''Write a class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances
'''

import json
from os import path


class FileStorage():
    '''creating class'''
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        '''init'''

    def all(self):
        '''return a dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''sets in obj the obj with key'''
        obj_name = "{obj.__class__.__name__}.{self.id}"
        self.__objects[obj_name] = obj

    def save(self):
        '''serialize __obj to the json file'''
        with open(file.json, "w", encoding="utf-8") as f:
            json.dump(self.__objects, f)

    def reload(self):
        '''deserialize json file to __obj'''
        path = "json.file"
        if path.exists(path) is False:
            return
        else:
            with open(path, "r", encoding="utf-8") as f:
                __objects = json.load(f)
            return __objects
