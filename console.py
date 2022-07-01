#!/usr/bin/python3
'''contains the entry point of the command interpreter'''

import cmd
import models
from models.base_model import BaseModel
import json
from models.engine.file_storage import FileStorage
import os
from models.user import User

all_classes = {"BaseModel": BaseModel, "User": User}

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
        if len(args) == 0 or args == None or args == "":
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
        classname = "BaseModel"
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] == classname:
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
        classname = "BaseModel"
        filename = "file.json"
        checker = 0
        if len(args) == 0:
            print("** class name missing **")
        if len(args) == 1 and args[0] != clasname:
            print("** class doesn't exist **")
        if len(args) == 1:
            print("** instance id missing **")
        if len(args) == 2:
            if os.path.isfile(filename) is True:
                new_dic = models.storage.all()
                dic_copy = new_dic.copy()
                key_id = f"{args[0]}.{args[1]}"
                for key, value in dic_copy.items():
                    if key_id == key:
                        del new_dic[key]
                        models.storage.save()
                        checker = 1
                if checker == 0:
                    print("** no instance found **")
 

    def do_all(self, arg):
        '''function that returns a str repr of all instances'''
        classname = "BaseModel"
        args = arg.split()
        data_instances = []
        if len(args) == 0:
            data = models.storage.all()
            for key, value in data.items():
                data_to_show = f"{str(data[key])}"
                data_instances.append(data_to_show)
            print(data_instances)
        elif args[0] != classname and len(args) == 1:
            print("** class doesn't exist **")
        elif args[0] == classname:
            data = models.storage.all()
            for key, value in data.items():
                data_to_show = f"{str(data[key])}"
                data_instances.append(data_to_show)
            print(data_instances)


    def do_update(self, arg):
        '''Update an instance based on cls name and id and add new attr'''
        args = arg.split()
        classname = "BaseModel"
        checker = 0

        if len(args) < 4:
            if len(args) == 0:
                print("** class name missing **")
            if len(args) == 1:
                if args[0] == classname:
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


    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
