#!/usr/bin/python3
'''contains the entry point of the command interpreter'''

import cmd
import models
from models.base_model import BaseModel
import json
from models.engine.file_storage import FileStorage
import os


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
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif args[0] == "BaseModel":
            new_inst = eval(classname)()
            new_inst.save()
            print(new_inst.id)

    def do_show(self, arg):
        '''print str repr of an inst based on the clss name and id'''
        filename = "file.json"
        args = arg.split()
        classname = "BaseModel"
        if len(args) == 0 or args == None or type(args[0]) is not str:
            print("** class name missing **")
            return
        if args[0] != classname:
            print("** class doesn't exist **")
            return
        if len(args) == 1 or args[1] == None:
            print("** instance id missing **")
            return
        else:
            data = models.storage.all()
            key = f"{args[0]}.{args[1]}"
            for key, value in data.items():
                if key in data:
                    print(data[key])
            if key not in data:
                print("** no instance found **")


    def do_destroy(self, arg):
        '''Deletes an instance based on the class name and id'''
        args = arg.split()
        classname = "BaseModel"
        filename = "file.json"
        checker = 0
        if len(args) == 0 or args == None or type(args[0]) is not str:
            print("** class name missing **")
            return
        if args[0] == None or args[0] != classname:
            print("** class doesn't exist **")
            return
        if len(args) == 1 or args[1] == None:
            print("** instance id missing **")
            return
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



if __name__ == '__main__':
    HBNBCommand().cmdloop()
