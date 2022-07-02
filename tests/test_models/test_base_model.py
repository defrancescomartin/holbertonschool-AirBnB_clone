#!/usr/bin/python3

''' Module tests/test_models/test_base_model'''

import unittest
import models
from datetime import datetime
from models.base_model import BaseModel
import json

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

    def test_bm_instance(self):
        '''Test instantiation of BaseModel class'''
        obj = BaseModel()
        self.assertEqual(type(obj), BaseModel)
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))

if __name__ == '__main__':
    unittest.main()
