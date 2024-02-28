#!/usr/bin/python3

"""
    The Console
"""

import cmd
from models import storage
from models import class_list
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_EOF(self, argv):
        "EOF command to exit the program"
        return True

    def do_quit(self, argv):
        "Quit command to exit the program"
        return True

    def do_salamarzu(self, argv):
        "SalamArzu command to say hello Arzu"
        print("Salam Arzu")

    def emptyline(self):
        pass

    def isArgumentValid(self, argv, validator_key):
        argv = argv.split()
        if len(argv) == 0 and validator_key < 5:
            print("** class name missing **")
            return False
        elif len(argv) == 0 and validator_key == 5:
            print([str(obj) for obj in storage.all().values()])
        elif argv and argv[0] not in class_list:
            print("** class doesn't exist **")
            return False
        elif argv and argv[0] in class_list and validator_key == 5:
            print([str(obj) for obj in storage.all().values() if
                   obj.__class__.__name__ == argv[0]])
        elif len(argv) == 1 and validator_key > 1 and validator_key < 5:
            print("** instance id missing **")
            return False
        elif len(argv) == 2 and validator_key > 1:
            try:
                a = storage.all()[f"{argv[0]}.{argv[1]}"]

                if validator_key == 2:
                    print(a)
                elif validator_key == 3:
                    storage.all().pop(f"{argv[0]}.{argv[1]}")
                    storage.save()
                elif validator_key == 4:
                    print("** attribute name missing **")
            except Exception:
                print("** no instance found **")
                return False

        elif len(argv) == 3:
            print("** value missing **")
        elif len(argv) == 4:
            key = f"{argv[0]}.{argv[1]}"
            try:
                instance = storage.all()[key]
            except Exception:
                print("** no instance found **")
                return False
            attribute_name = argv[2]
            attribute_value = argv[3]

            if attribute_value.isdigit():
                setattr(instance, attribute_name, int(attribute_value))
            else:
                try:
                    setattr(instance, attribute_name, float(attribute_value))
                except Exception:
                    attribute_value = attribute_value[1:-1]
                    setattr(instance, attribute_name, str(attribute_value))

            instance.save()

        return True

    def do_create(self, argv):
        if self.isArgumentValid(argv, 1):
            b1 = eval(argv)()
            b1.save()
            print(b1.id)

    def do_show(self, argv):
        self.isArgumentValid(argv, 2)

    def do_destroy(self, argv):
        self.isArgumentValid(argv, 3)

    def do_update(self, argv):
        self.isArgumentValid(argv, 4)

    def do_all(self, argv):
        self.isArgumentValid(argv, 5)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
