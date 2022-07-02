#!/usr/bin/python3

import unittest
from models.state import Place
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models


class TestPlace(unittest.TestCase):
    '''class to test Place'''


city_id: string - empty string: it will be the City.id
user_id: string - empty string: it will be the User.id
name: string - empty string
description: string - empty string
number_rooms: integer - 0
number_bathrooms: integer - 0
max_guest: integer - 0
price_by_night: integer - 0
latitude: float - 0.0
longitude: float - 0.0
amenity_ids: list of string - empty list: it will be the list of Amenity.id
later
