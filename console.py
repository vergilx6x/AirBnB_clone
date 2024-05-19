#!/usr/bin/python3
import cmd
import shlex
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):

    prompt = ("(hbnb) ")

    def do_greet(self, line):
        names = shlex.split(line)
        for name in names:
            print(f'Hello {name}')

    def do_sum(self, line):
        nums = line.split()
        print(nums)
        nums = list(map(int, nums))
        print(nums)
        total = sum(nums)
        print(total)

    def do_create(self, line):
        if line == "BaseModel":
            obj_cls = BaseModel()
            obj_cls.save()

    def do_show(self, line):
        class_name, class_id = line.split()
        obj_name = (class_name + "." + class_id)
        obj_dict = storage.all()
        for key, v in obj_dict.items():
            if obj_dict[key] == obj_name:
                print(obj_dict[key])

    def emptyline(self):

        pass

    def do_EOF(self, line):
        print()
        return True

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
