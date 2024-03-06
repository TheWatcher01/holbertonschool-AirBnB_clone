#!/usr/bin/python3
"""This module contains the HBNBCommand class for the console"""


import cmd
import models


class HBNBCommand(cmd.Cmd):
    """
    This class contains the console for the HBNB project
    """

    prompt = "(hbnb) "

    def obj_arg_valid(self, args):
        if (not args):
            print("** class name missing **")
            return False
        length = len(args)
        if (length < 1):
            print("** class name missing **")
            return False
        if (not models.storage.class_exists(args[0])):
            print("** class doesn't exist **")
            return False
        if (length < 2):
            print("** instance id missing **")
            return False
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            _class = models.storage.get_class(arg)
            if (not _class):
                print("** class doesn't exist **")
                return
            new_instance = _class()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = arg.split()
        if (self.obj_arg_valid(args) is False):
            return
        class_name = args[0]
        instance_id = args[1]
        instance = models.storage.get(class_name, instance_id)
        if instance:
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if (self.obj_arg_valid(args) is False):
            return
        class_name = args[0]
        instance_id = args[1]
        instance = models.storage.get(class_name, instance_id)
        if instance:
            models.storage.delete(instance)
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all instances"""
        if not arg:
            instances = models.storage.all()
            print([str(instance) for instance in instances.values()])
        else:
            _class = models.storage.get_class(arg)
            if (not _class):
                print("** class doesn't exist **")
                return
            all = models.storage.all()
            instances = []
            for key in all:
                instance = all[key]
                if instance.__class__ == _class:
                    instances.append(str(instance))
            print([str(instance) for instance in instances])

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        args = arg.split()
        if (self.obj_arg_valid(args) is False):
            return
        class_name = args[0]
        instance_id = args[1]
        instance = models.storage.get(class_name, instance_id)
        if instance:
            if len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                attribute_name = args[2]
                attribute_value = args[3]
                attribute_type = type(getattr(instance, attribute_name))
                setattr(instance, attribute_name, attribute_type(attribute_value))
                instance.save()
        else:
            print("** no instance found **")

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
