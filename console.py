#!/usr/bin/python3
'''contains the entry point of the command interpreter'''

import cmd
import models
from models.base_model import BaseModel
import json
from models.engine.file_storage import FileStorage
import os
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


all_classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}


class HBNBCommand(cmd.Cmd):
    '''command interpreter'''

    prompt = '(hbnb) '

    def do_quit(self, arg):
        '''to exit the program'''
        return True

    def do_EOF(self, arg):
        '''exit the program'''
        return True

    def help_quit(self):
        '''updated and documented help'''
        print('Quit command to exit the program')

    def help_EOF(self):
        '''updated and documented help'''
        print('EOF commando to exit')

    def emptyline(self):
        '''empty line + ENTER shouldn't execute anything'''
        pass

    def do_create(self, arg):
        '''function that creates a new instance of BM, save it and print it'''
        args = arg.split()
        classname = "BaseModel"
        if len(args) == 0 or args is None or args == "":
            print("** class name missing **")
        if args[0] in all_classes:
            new_inst = all_classes[args[0]]()
        else:
            print("** class doesn't exist **")
            return False
        print(new_inst.id)
        new_inst.save()

    def do_show(self, arg):
        '''print str repr of an inst based on the clss name and id'''
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in all_classes:
            if len(args) > 1:
                key = f"{args[0]}.{args[1]}"
                data = models.storage.all()
                if key in data:
                    print(data[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        '''Deletes an instance based on the class name and id'''
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in all_classes:
            if len(args) > 1:
                key = f"{args[0]}.{args[1]}"
                data = models.storage.all()
                if key in data:
                    data.pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        '''function that returns a str repr of all instances'''
        args = arg.split()
        data = models.storage.all()
        data_instances = []

        if len(args) == 0:
            for key, value in data.items():
                data_instances.append(str(value))
            print(data_instances)
        elif args[0] not in all_classes and len(args) == 1:
            print(" class doesn't exist ")
        else:
            for key, value in data.items():
                if args[0] in key:
                    data_instances.append(str(value))
            print(data_instances)

    def do_update(self, arg):
        '''Update an instance based on cls name and id and add new attr'''
        args = arg.split()
        checker = 0

        if len(args) < 4:
            if len(args) == 0:
                print("** class name missing **")
            if len(args) == 1:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
            if len(args) == 2:
                data = models.storage.all()
                key_id = f"{args[0]}.{args[1]}"
                for key, value in data.items():
                    if key_id == key:
                        print("** attribute name missing **")
                        checker = 1
                if checker == 0:
                    print("** no instance found **")
            if len(args) == 3:
                print("** value missing **")
        if len(args) == 4:
            data = models.storage.all()
            key_id = f"{args[0]}.{args[1]}"
            for key, value in data.items():
                if key_id == key:
                    if args[3] == key:
                        setattr(value, args[2], args[3])
                        models.storage.save()
                    else:
                        setattr(value, args[2], args[3])
                        models.storage.save()
        elif len(args) > 4:
            data = models.storage.all()
            key_id = f"{args[0]}.{args[1]}"
            for key, value in data.items():
                if key_id == key:
                    if args[3] == key:
                        setattr(value, args[2], args[3])
                        models.storage.save()
                    else:
                        setattr(value, args[2], args[3])
                        models.storage.save()

    def do_count(self, arg):
        ''' Count and return the number of instances of a class'''
        if arg in all_classes:
            i = 0
            data = models.storage.all()
            for key, value in data.items():
                if arg in key:
                    i = i + 1
            print(i)
        else:
            print ("** class doesn't exist **")

    def default(self, arg):
        delimiter = arg.split(".")
        class_part = delimiter[0]
        function = delimiter[1]

        if class_part in all_classes and function == "all()":
            HBNBCommand.do_all(self, class_part)
        elif class_part in all_classes and function == "count()":
            HBNBCommand.do_count(self, class_part)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
