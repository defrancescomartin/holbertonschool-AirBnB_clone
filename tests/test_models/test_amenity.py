#!/usr/bin/python3

import unittest
from models.state import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models


class TestAmenity(unittest.TestCase):
    '''class to test Amenity'''

    def test_doc(self):
        '''method to check if it has documentation'''
        self.assertIsNotNone(Amenity.__doc__)

    def test_subclass(self):
        '''method to check subclasses'''
        self.assertEqual(issubclass(Amenity, BaseModel), True)
        self.assertEqual(issubclass(Amenity, basemodel), False)

    def test_instance(self):
        '''method to check for instances'''
        Amenity_1 = Amenity()
        self.assertEqual(isinstance(Amenity_1, Amenity), True)
        self.assertEqual(isinstance(Amenity_1, amenity), False)

    def test_id(self):
        '''method to check for id'''
        Amenity_2 = Amenity()
        Amenity_3 = Amenity()
        self.assertNotEqual(Amenity_3.id, Amenity_2.id)

    def test_creationofinstance(self):
        '''method to check the creation of the instance'''
        Amenity_4 = Amenity()
        self.assertTrue(hasattr(Amenity_4, "__init__"))
        self.assertTrue(hasattr(Amenity_4, "id"))
        self.assertTrue(hasattr(Amenity_4, "created_at"))
        self.assertTrue(hasattr(Amenity_4, "updated_at"))

    def test_attrname(self):
        '''method to check attr name'''
        example = Amenity()
        example.name = "Kitchen"
        self.assertTrue(type(example.name), str)
        self.assertTrue("name" in example.__dict__)
        self.assertFalse("location" in example.__dict__)


if __name__ == "__main__":
    unittest.main()
