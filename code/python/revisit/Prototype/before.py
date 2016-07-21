"""
http://gameprogrammingpatterns.com/prototype.html
http://en.wikipedia.org/wiki/Prototype_pattern
"""

from abc import ABCMeta, abstractmethod

## Monster ##

class Monster(object):
    pass

class Ghost(Monster):
    pass

class Demon(Monster):
    pass

class Sorcerer(Monster):
    pass

## Spawner ##

class Spawner(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def spawnMonster(self):
        pass

class GhostSpawner(Spawner):
    def spawnMonster(self):
        return Ghost()

class DemonSpawner(Spawner):
    def spawnMonster(self):
        return Demon()

class SorcererSpawner(Spawner):
    def spawnMonster(self):
        return Sorcerer()
