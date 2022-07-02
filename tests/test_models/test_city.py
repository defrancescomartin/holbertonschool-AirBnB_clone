#!/usr/bin/python3

import unittest
from models.city import City
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models


class TestCity(unittest.TestCase):
    '''class to test City'''

    def test_doc(self):
        '''method to check if it has documentation'''
        self.assertIsNotNone(City.__doc__)

    def test_subclass(self):
        '''method to check subclasses'''
        self.assertEqual(issubclass(City, BaseModel), True)
        self.assertEqual(issubclass(City, FileStorage), False)

    def test_instance(self):
        '''method to check for instances'''
        Montevideo = City()
        self.assertEqual(isinstance(Montevideo, City), True)

    def test_id(self):
        '''method to check for id'''
        Canelones = City()
        Piriapolis = City()
        self.assertNotEqual(Canelones.id, Piriapolis.id)

    def test_creationofinstance(self):
        '''method to check the creation of the instance'''
        Atlantida = City()
        self.assertTrue(hasattr(Atlantida, "__init__"))
        self.assertTrue(hasattr(Atlantida, "id"))
        self.assertTrue(hasattr(Atlantida, "created_at"))
        self.assertTrue(hasattr(Atlantida, "updated_at"))

    def test_attrname(self):
        '''method to check attr name'''
        example = City()
        example.name = "Minas"
        self.assertTrue(type(example.name), str)
        self.assertTrue("name" in example.__dict__)
        self.assertFalse("location" in example.__dict__)

    def test_stateid(self):
        '''method to check attr id'''
        example1 = City()
        example1.state_id = "ParquedelPlata"
        self.assertTrue(type(example1.id), str)
        self.assertTrue("state_id" in example1.__dict__)


if __name__ == "__main__":
    unittest.main()
