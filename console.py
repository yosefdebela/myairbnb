#!/usr/bin/python3

import cmd
import sys

from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.state import State



class MyConsole(cmd.Cmd):
    intro = "welcome to my trial console project"
    prompt = "trial>>"
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}
    def do_create(self, arg):
        """
        Create a new instance of BaseModel
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]

        if class_name not in self.class_dict:
            print("** class doesn't exist **")
            return
        new_instance = self.class_dict[class_name]()
        for attr_pair in args[1:]:
            if '=' in attr_pair:
                key, value = attr_pair.split('=', 1)
                # Handle quoted strings (with underscores representing spaces)
                if value.startswith('"') and value.endswith('"'):
                    value = value.strip('"').replace('_', ' ')
                elif value.isdigit():
                    value = int(value)
                else:
                    try:
                        value = float(value)
                    except ValueError:
                        continue  # Skip invalid values
                setattr(new_instance, key, value)

        new_instance.save()
        print(new_instance.id)
    def do_quit(self, arg):
        return True
    def do_exit(self):
        return True
    def do_all(self, line):
        """Prints all string representation of all instances.
        """
        if line != "":
            words = line.split(' ')
            if words[0] not in self.class_dict:
                print("** class doesn't exist **")
            else:
                nl = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == words[0]]
                print(nl)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)



if __name__ == "__main__":
    MyConsole().cmdloop()