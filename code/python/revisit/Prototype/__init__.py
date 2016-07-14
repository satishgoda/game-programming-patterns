
"""
http://gameprogrammingpatterns.com/prototype.html
http://en.wikipedia.org/wiki/Prototype_pattern
"""

import before
import after

def usage():
    """
    import Prototype

    print Prototype.usage()

    try:
        eval(Prototype.usage())
    except SyntaxError as e:
        pass

    results = {}

    exec Prototype.usage() in results

    print results.keys()

    :return: python code string
    """
    return """
import Prototype

ghost1 = Prototype.after.Ghost(100, 45)

ghost1.clone()

spawnedGhost = Prototype.after.Spawner(Prototype.after.Ghost(100, 45)).spawnMonster()
    """
