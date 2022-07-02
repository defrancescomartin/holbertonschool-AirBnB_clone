#!/usr/bin/python3

''' Module tests/test_models/test_base_model'''

import unittest
import modules
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):

    def test_doc(self):
        '''Test Docstring'''
        self.assertIsNotNone(BaseModel.__doc__)

    def test_str(self):
        '''Test str method'''
        model = BaseModel()
        model_str = (
            f'[{BaseModel.__name__}], ({model.id}),<{model.__dict__}>')
        self.assertEqual(model_str, str(model))

    def test_save(self):
        '''Test save method'''
        obj = BaseModel()
        created = obj.created_at
        uptdated = obj.updated_at
        obj.save()
        created2 = obj.created_at
        update2 = obj.updated_at

        self.assertEqual(created, created2)
        self.assertNotEqual(updated, updated2)

    def test_to_dict(self):
        '''Test to_dict method'''
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_base_model(self):
        '''Test BaseModel object creation based on task3'''
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        # checking attribute types and class
        self.assertEqual(type(my_model), BaseModel)
        # check id
        self.assertTrue(hasattr(my_model, "id"))
        self.assertEqual(type(my_model.id), str)
        # check created_at
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertEqual(type(my_model.created_at), datetime)
        # check updated_at
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertEqual(type(my_model.updated_at), datetime)
        # check my_number
        self.assertTrue(hasattr(my_model, "my_number"))
        self.assertEqual(type(my_model.my_number), int)
        # check name
        self.assertTrue(hasattr(my_model, "name"))
        self.assertEqual(type(my_model.name), str)
        my_model.save()
        my_model_json = my_model.to_dict()
        # checking if return is dict and datetimes to str and __class__
        self.assertTrue((type(my_model_json)) == dict)
        self.assertEqual(type(my_model_json['created_at']), str)
        self.assertIsInstance(my_model_json['updated_at'], str)
        self.assertEqual(my_model_json['__class__'], 'BaseModel')
        # checking saves correctly and updates updated_at attr
        # generic name
        my_model.name = "John Doe"
        my_model.save()
        # create 2nd json
        sec_json = my_model.to_dict()
        self.assertNotEqual(my_model_json['name'], sec_json['name'])
        self.assertNotEqual(my_model.created_at, my_model.updated_at)
        self.assertEqual(my_model_json['created_at'], sec_json['created_at'])
        new_obj = BaseModel(**sec_json)
        new_obj.save()
        new_json = new_obj.to_dict()
        self.assertEqual(sec_json['name'], new_json['name'])
        self.assertEqual(sec_json['created_at'], new_json['created_at'])
        self.assertNotEqual(sec_json['updated_at'], new_json['updated_at'])


if __name__ == '__main__':
    unittest.main()