from abc import ABCMeta, abstractmethod

from actions import jump, fireGun, swapWeapon, lurchIneffectively
from keys import BUTTON_X, BUTTON_Y, BUTTON_A, BUTTON_B


class Command(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self):
        pass


class JumpCommand(Command):
    def execute(self):
        jump()


class FireCommand(Command):
    def execute(self):
        fireGun()


class SwapCommand(Command):
    def execute(self):
        swapWeapon()


class LurchIneffectivelyCommand(Command):
    def execute(self):
        lurchIneffectively()


class InputHandler(object):

    def __init__(self):
        self._buttonX = JumpCommand()
        self._buttonY = FireCommand()
        self._buttonA = SwapCommand()
        self._buttonB = LurchIneffectivelyCommand()

    def handleInput(self):
        if isPressed(BUTTON_X):
            self._buttonX.execute()
        elif isPressed(BUTTON_Y):
            self._buttonY.execute()
        elif isPressed(BUTTON_A):
            self._buttonA.execute()
        elif isPressed(BUTTON_B):
            self._buttonB.execute()
