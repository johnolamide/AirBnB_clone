#!/usr/bin/python3
""" Module contains the class definition for the HBNBCommand class
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand (cmd.Cmd): commandline interface
        Attributes:
            prompt (string): custom prompt
        Methods:
            do_quit(self, arg): quit the commandline
            do_EOF(self, arg): handles EOF
            emptyline(self): ignores emptyline command
            do_create(self, arg):
            do_show(self, arg):
            do_destroy(self, arg):
            do_all(self, arg):
            do_update(self, arg):
    """
    prompt = "(hbnb) "
    className = ["BaseModel"]

    def do_quit(self, arg):
        """ Quit the commandline
        """
        return True

    def do_EOF(self, arg):
        """ Handles EOF
        """
        return True

    def emptyline(self):
        """ Ignores emptyline command
        """
        pass

    def do_create(self, arg):
        """
        """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.className:
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.className:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            objs = storage.all()
            if key in objs:
                print(objs[key])
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
