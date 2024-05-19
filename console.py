#!/usr/bin/python3
"""Defines the AirBnB_clone console"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnb_clone
    storage handling.

    Attributes:
    prompt : Command prompt.
    classes : Available classes.
    """

    prompt = ("(hbnb) ")
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }

    obj_dict = storage.all()

    def do_create(self, arg):
        """Creates a class and prints it's id.
        Usage: create <class>
        """
        if (arg):
            class_name = arg
            if arg in HBNBCommand.classes:
                new_obj = HBNBCommand.classes[class_name]()
                print(new_obj.id)
                storage.save()
            elif arg not in HBNBCommand.classes:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Display the string representation of a class.
        Usage: show <class> <id>
        """
        args = arg.split()
        if not (args):
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class name doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """Deletes a class.
        Usage: destroy <class> <id>
        """
        args = arg.split()
        if not (args):
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class name doesn't exist **")
        elif not arg[1]:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """Display string representation of all classes,
        or a specific type.
        Usage : all or all <class>
        """
        args = arg.split()
        if len(args) > 0 and args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif not(args):
                    obj_list.append(obj.__str__())
            print(obj_list)

    def do_update(self, arg):
        """Updates a class"""
        obj_dict = storage.all()
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(args) == 4:
            obj = obj_dict["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = valtype(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = obj_dict["{}.{}".format(args[0], args[1])]
            for k, v in eval(args[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    value_type = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = value_type(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

    def emptyline(self):
        """Do nothing when reveiving an empty line."""
        pass

    def do_EOF(self, line):
        """EOF signal to exit the program."""
        print()
        return True

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
