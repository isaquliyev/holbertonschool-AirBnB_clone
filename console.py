#!/usr/bin/python3

"""
    The Console
"""

import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
