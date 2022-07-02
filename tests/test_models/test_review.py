#!/usr/bin/python3

import unittest
from models.state import Review
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models


class TestReview(unittest.TestCase):
    '''class to test Review'''

    def test_doc(self):
        '''method to check if it has documentation'''
        self.assertIsNotNone(Review.__doc__)

    def test_subclass(self):
        '''method to check subclasses'''
        self.assertEqual(issubclass(Review, BaseModel), True)
        self.assertEqual(issubclass(Review, basemodel), False)

    def test_instance(self):
        '''method to check for instances'''
        review_1 = Review()
        self.assertEqual(isinstance(review_1, Review), True)
        self.assertEqual(isinstance(review_1, review), False)

    def test_id(self):
        '''method to check for id'''
        review_2 = Review()
        review_3 = Review()
        self.assertNotEqual(review_2.id, review_3.id)

    def test_creationofinstance(self):
        '''method to check the creation of the instance'''
        review_4 = Review()
        self.assertTrue(hasattr(review_4, "__init__"))
        self.assertTrue(hasattr(review_4, "id"))
        self.assertTrue(hasattr(review_4, "created_at"))
        self.assertTrue(hasattr(review_4, "updated_at"))

    def test_attrtext(self):
        '''method to check attr name'''
        example = Review()
        example.text = "comment"
        self.assertTrue(type(example.text), str)
        self.assertTrue("text" in example.__dict__)
        self.assertFalse("box" in example.__dict__)

    def test_placeid(self):
        '''method to check attr id'''
        example1 = Review()
        example1.place_id = "ParquedelPlata"
        self.assertTrue(type(example1.place_id), str)
        self.assertTrue("palce_id" in example1.__dict__)

    def test_userid(self):
        '''method to check attr id'''
        example2 = Review()
        example2.user_id = "Juan"
        self.assertTrue(type(example2.user_id), str)
        self.assertTrue("user_id" in example2.__dict__)


if __name__ == "__main__":
    unittest.main()
