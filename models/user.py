#!/usr/bin/python3

'''class User that inherit from BaseModel'''

from models.base_model import BaseModel


class User(BaseModel):

    '''Public class attributes: '''
    '''email, password, first name, last name: empty strings'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
