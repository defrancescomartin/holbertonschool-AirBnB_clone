#!/usr/bin/python3
'''contains the entry point of the command interpreter'''

import cmd
import models
from models.base_model import BaseModel


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
        args = arg.split()
        classname = "BaseModel"
        if len(args) == 0 or args == None:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] == "BaseModel" and args[1] == 


if __name__ == '__main__':
    HBNBCommand().cmdloop()
