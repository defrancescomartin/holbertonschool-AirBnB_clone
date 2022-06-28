#!/usr/bin/python3
'''contains the entry point of the command interpreter'''

import cmd
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):