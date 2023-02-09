#!/usr/bin/python3
# AUTHOR: Mezie Gift
"""This module defines the HBnB console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """A Command processor class"""
    prompt = '(hbnb)'

    def do_EOF(self, line):
        """End of file"""
        return True

    def empty_line(self, line):
        """Do nothing"""

    def do_quit(self, line):
        """Exit the command processor"""
        exit()
# to be updated

if __name__ == '__main__':
    HBNBCommand().cmdloop()
