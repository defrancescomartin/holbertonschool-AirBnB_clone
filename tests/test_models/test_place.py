#!/usr/bin/python3

import unittest
from models.place import Place
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models


class TestPlace(unittest.TestCase):
    '''class to test Place'''

    def test_doc(self):
        '''method to check if it has documentation'''
        self.assertIsNotNone(Place.__doc__)

    def test_subclass(self):
        '''method to check subclasses'''
        self.assertEqual(issubclass(Place, BaseModel), True)
        self.assertEqual(issubclass(Place, FileStorage), False)

    def test_instance(self):
        '''method to check for instances'''
        place_1 = Place()
        self.assertEqual(isinstance(place_1, Place), True)

    def test_id(self):
        '''method to check for id'''
        place_2 = Place()
        place_3 = Place()
        self.assertNotEqual(place_2.id, place_3.id)

    def test_creationofinstance(self):
        '''method to check the creation of the instance'''
        place_4 = Place()
        self.assertTrue(hasattr(place_4, "__init__"))
        self.assertTrue(hasattr(place_4, "id"))
        self.assertTrue(hasattr(place_4, "created_at"))
        self.assertTrue(hasattr(place_4, "updated_at"))

    def test_attrname(self):
        '''method to check attr name'''
        example = Place()
        example.name = "place"
        self.assertTrue(type(example.name), str)
        self.assertTrue("name" in example.__dict__)
        self.assertFalse("box" in example.__dict__)

    def test_cityid(self):
        '''method to check attr id'''
        example1 = Place()
        example1.city_id = "ParquedelPlata"
        self.assertTrue(type(example1.city_id), str)
        self.assertTrue("city_id" in example1.__dict__)

    def test_userid(self):
        '''method to check attr id'''
        example2 = Place()
        example2.user_id = "Juan"
        self.assertTrue(type(example2.user_id), str)
        self.assertTrue("user_id" in example2.__dict__)

    def test_attrdescription(self):
        '''method to check attr name'''
        example3 = Place()
        example3.description = "place"
        self.assertTrue(type(example3.description), str)
        self.assertTrue("description" in example3.__dict__)
        self.assertFalse("box" in example3.__dict__)

    def test_attrrooms(self):
        '''method to check attr name'''
        example4 = Place()
        example4.number_rooms = 2
        self.assertTrue(type(example4.number_rooms), int)
        self.assertTrue("number_rooms" in example4.__dict__)
        self.assertFalse("box" in example4.__dict__)

    def test_attrbathrooms(self):
        '''method to check attr name'''
        example5 = Place()
        example5.number_bathrooms = 2
        self.assertTrue(type(example5.number_bathrooms), int)
        self.assertTrue("number_bathrooms" in example5.__dict__)
        self.assertFalse("box" in example5.__dict__)

    def test_attrguest(self):
        '''method to check attr name'''
        example6 = Place()
        example6.max_guest = 2
        self.assertTrue(type(example6.max_guest), int)
        self.assertTrue("max_guest" in example6.__dict__)
        self.assertFalse("box" in example6.__dict__)

    def test_attrprice(self):
        '''method to check attr name'''
        example7 = Place()
        example7.price_by_night = 25
        self.assertTrue(type(example7.price_by_night), int)
        self.assertTrue("price_by_night" in example7.__dict__)
        self.assertFalse("box" in example7.__dict__)

    def test_attrlatitude(self):
        '''method to check attr name'''
        example8 = Place()
        example8.latitude = 50.5
        self.assertTrue(type(example8.latitude), float)
        self.assertTrue("latitude" in example8.__dict__)
        self.assertFalse("box" in example8.__dict__)

    def test_attrlongitude(self):
        '''method to check attr name'''
        example9 = Place()
        example9.longitude = 49.8
        self.assertTrue(type(example9.longitude), float)
        self.assertTrue("longitude" in example9.__dict__)
        self.assertFalse("box" in example9.__dict__)

    def test_attramenity(self):
        '''method to check attr name'''
        example10 = Place()
        example10.amenity_ids = ["Bathroom", "Bedroom"]
        self.assertTrue(type(example10.amenity_ids), list)
        self.assertTrue("amenity_ids" in example10.__dict__)
        self.assertFalse("box" in example10.__dict__)


if __name__ == "__main__":
    unittest.main()
