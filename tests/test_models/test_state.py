#!/usr/bin/python3

import unittest
from models.state import State
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models


class TestState(unittest.TestCase):
    '''class to test State'''

    def test_doc(self):
        '''method to check if it has documentation'''
        self.assertIsNotNone(State.__doc__)

    def test_subclass(self):
        '''method to check subclasses'''
        self.assertEqual(issubclass(State, BaseModel), True)
        self.assertEqual(issubclass(State, basemodel), False)

    def test_instance(self):
        '''method to check for instances'''
        Montevideo = State()
        self.assertEqual(isinstance(Montevideo, State), True)
        self.assertEqual(isinstance(Montevideo, state), False)

    def test_id(self):
        '''method to check for id'''
        Canelones = State()
        Maldonado = State()
        self.assertNotEqual(Montevideo.id, Maldonado.id)

    def test_creationofinstance(self):
        '''method to check the creation of the instance'''
        Colonia = State()
        self.assertTrue(hasattr(Colonia, "__init__"))
        self.assertTrue(hasattr(Colonia, "id"))
        self.assertTrue(hasattr(Colonia, "created_at"))
        self.assertTrue(hasattr(Colonia, "updated_at"))

    def test_attrname(self):
        '''method to check attr name'''
        example = State()
        example.name = "Salto"
        self.assertTrue(type(example.name), str)
        self.assertTrue("name" in example.__dict__)
        self.assertFalse("location" in example.__dict__)


if __name__ == "__main__":
    unittest.main()
