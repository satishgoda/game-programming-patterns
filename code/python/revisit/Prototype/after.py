"""
http://stackoverflow.com/questions/11217878/python-2-7-combine-abc-abstractmethod-and-classmethod
"""

from abc import ABCMeta, abstractmethod


class Monster(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def clone(self):
        pass

class Ghost(Monster):
    def __init__(self, health, speed):
        self._health = health
        self._speed = speed

    def clone(self):
        return self.__class__(self._health, self._speed)

    def __repr__(self):
        return "Instance of {0} at {1}: _health={2}  _speed={3}".format(self.__class__, hex(id(self)), self._health, self._speed)

class Spawner(object):
    def __init__(self, monsterPrototype):
        self._monsterPrototype = monsterPrototype

    def spawnMonster(self):
        return self._monsterPrototype.clone()

if __name__ == '__main__':
    try:
        Monster()
    except TypeError as e:
        print e

    ghost1 = Ghost(100, 45)
    print ghost1
    print ghost1.clone()

    fastestGhostPrototype = Ghost(100, 100)
    fastestGhostSpawner = Spawner(fastestGhostPrototype)

    print fastestGhostSpawner.spawnMonster()
