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
            do_create(self, arg): create a new instance
            do_show(self, arg): show the instance properties using it's id
            do_destroy(self, arg): destroys an instance
            do_all(self, arg): return all instances
            do_update(self, arg): updates an instance
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
        """ Create a new Instance and prints out the id
            Example:
                (HBNB) create <class name>
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
        """ Shows instance property from id
            Example:
                (HBNB) show <class name> <instance id>
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

    def do_destroy(self, arg):
        """ Destroys an instance
            Example:
                (HBNB) destroy <class name> <instance id>
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
                del objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """ Returns all instances
            Example:
                (HBNB) all <class name>
        """
        args = arg.split()
        if not args or args[0] in HBNBCommand.className:
            objs = storage.all()
            obj_list = []
            for obj in objs.values():
                obj_list.append(str(obj))
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """ Updates the property of an instance
            Example:
                (HBNB) update <class name> <instance id> <property name> <property value>
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
                obj = objs[key]
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    attr_name = args[2]
                    attr_value = args[3].strip('"')

                    if attr_name not in ["id", "created_at", "updated_at"]:
                        obj[attr_name] = str(attr_value)
                        storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
