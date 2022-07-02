#!/usr/bin/python3

import unittest
from models.state import Review
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models


class TestReview(unittest.TestCase):
    '''class to test Review'''


place_id: string - empty string: it will be the Place.id
user_id: string - empty string: it will be the User.id
text: string - empty string
