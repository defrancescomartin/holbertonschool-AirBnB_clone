#!/usr/bin/python3
'''contains the entry point of the command interpreter'''

import cmd
import models
from models.base_model import BaseModel
import json
from models.engine.file_storage import FileStorage


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
        '''print str repr of an inst based on the clss name and id
        FALTA MODIFICAR EL SHOW PARA QUE EL FORMATO DE LA FECHA QUEDE CORRECTO'''
        filename = "file.json"
        args = arg.split()
        new_dic = {}
        classname = "BaseModel"
        if len(args) == 0 or args == None or type(args[0]) is not str:
            print("** class name missing **")
        elif args[0] != classname:
            print("** class doesn't exist **")
        elif len(args) == 1 or args[1] == None:
            print("** instance id missing **")
        elif args[0] == classname:
            with open(filename, "r", encoding="utf-8") as f:
                new_dic = models.storage.all()
                for key in new_dic:
                    if key in new_dic:
                        print(new_dic[key])
                    else:
                        print("** no instance found **")

'''    def do_destroy(self, arg):
            Deletes an instance based on the class name and id
        args = arg.split()
        classname = "BaseModel"
        filename = "file.json"
        if len(args) == 0 or args == None or type(args[0]) is not str:
            print("** class name missing **")
        elif args[0] == None or args[0] != classname:
            print("** class doesn't exist **")
        elif len(args) == 1 or args[1] == None:
            print("** instance id missing **")
        elif args[0] == classname and len(args) == 2:
            with open(filename, "r", encoding="utf-8") as f:
                new_dic = json.load(f)
                for key, value in new_dic.items():
                    id_from_json = key.split('.')
                    if args[1] == id_from_json[1]:
'''




if __name__ == '__main__':
    HBNBCommand().cmdloop()
