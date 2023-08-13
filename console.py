#!/usr/bin/python3
""" Module contains the class definition for the HBNBCommand class
"""
import cmd


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
            default(self, line): override the default command
    """
    prompt = "(hbnb) "

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
        from models import models
        if not arg:
            print("** class name missing **")
        elif arg not in models:
            print("** class doesn't exist **")
        else:
            obj = models[arg]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """ Shows instance property from id
            Example:
                (HBNB) show <class name> <instance id>
        """
        from models import storage
        from models import models
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in models:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            class_name = args[0]
            obj_id = args[1]
            key = class_name + "." + obj_id
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
        from models import storage
        from models import models
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in models:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            class_name = args[0]
            obj_id = args[1]
            key = class_name + "." + obj_id
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
        from models import storage
        from models import models
        args = arg.split()
        objs = storage.all()
        obj_list = []
        if not args:
            obj_list = [obj.to_dict() for obj in objs.values()]
            print(obj_list)
        elif args[0] in models:
            obj_list = [obj.to_dict() for obj in objs.values()
                        if obj.to_dict().get("__class__") == args[0]]
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """ Updates the property of an instance
            Example:
                (HBNB) update <class name> <id> <property> <value>
        """
        from models import storage
        from models import models
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in models:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            class_name = args[0]
            obj_id = args[1]
            key = class_name + "." + obj_id
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
                        setattr(obj, attr_name, attr_value)
                        obj.save()
            else:
                print("** no instance found **")

    def count(self, arg):
        """ Count the number of instances
        """
        from models import models
        from models import storage
        objs = storage.all()
        if arg in models:
            obj_list = [obj.to_dict for obj in objs.values()
                        if obj.to_dict().get("__class__") == arg]
            print(len(obj_list))

    def default(self, line):
        """ Override the default command
            Args:
                line: command to execute
        """
        from models import models
        args = line.split(".")
        class_name = args[0]
        commands = {
            "all": self.do_all,
            "count": self.count,
            "show": self.do_show,
            "destroy": self.do_destroy
        }
        command_arg = args[1].replace('(', ' ')\
                             .replace(',', '').replace(')', ' ')\
                             .split()
        command = command_arg[0]
        if command in commands:
            if command in ["all", "count"]:
                commands[command](class_name)
            elif command in ["show", "destroy"]:
                commands[command](class_name + " " + command_arg[1])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
