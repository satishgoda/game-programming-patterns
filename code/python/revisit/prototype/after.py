"""
http://stackoverflow.com/questions/11217878/python-2-7-combine-abc-abstractmethod-and-classmethod
"""

from abc import ABCMeta, abstractmethod


class Monster(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def clone(cls):
        pass

class Ghost(Monster):
    @classmethod
    def clone(cls):
        return cls()

class Demon(Monster):
    pass

class Sorcerer(Monster):
    pass


if __name__ == '__main__':
    try:
        Monster()
    except TypeError as e:
        print e

    ghost1 = Ghost()
    print ghost1
    print ghost1.clone()
