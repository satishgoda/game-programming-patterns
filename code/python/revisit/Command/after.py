import sys
import argparse
from abc import ABCMeta, abstractmethod


class Actor(object):
    def jump(self):
        print "Jumping"

    def fireGun(self):
        print "Firing Gun"

    def swapWeapon(self):
        print "Swapping Weapon"

    def lurchIneffectively(self):
        print "Lurching Ineffectively"


class Command(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self, actor):
        pass


class DoNothingCommand(Command):
    def execute(self, actor):
        print "Doing nothing"


class JumpCommand(Command):
    def execute(self, actor):
        actor.jump()


class FireCommand(Command):
    def execute(self, actor):
        actor.fireGun()


class SwapCommand(Command):
    def execute(self, actor):
        actor.swapWeapon()


class LurchIneffectivelyCommand(Command):
    def execute(self, actor):
        actor.lurchIneffectively()


class InputHandler(object):

    def __init__(self):
        self._buttonX = JumpCommand()
        self._buttonY = FireCommand()
        self._buttonA = SwapCommand()
        self._buttonB = LurchIneffectivelyCommand()
        self._doNothing = DoNothingCommand()

    def handleInput(self):
        if isPressed(BUTTON_X):
            return self._buttonX
        elif isPressed(BUTTON_Y):
            return self._buttonY
        elif isPressed(BUTTON_A):
            return self._buttonA
        elif isPressed(BUTTON_B):
            return self._buttonB
        return self._doNothing


def registerButtons(buttons):
    for button in buttons:
        globals()[button] = False


def resetButtons():
    registerButtons(buttons)


def isPressed(button):
    return bool(button)


def isButton(button):
    return button if button in buttons else None


def handleButtonPressEvent():
    command = inputHandler.handleInput()
    command.execute(actor)
    resetButtons()


def processButton(button):
    if isButton(button):
        globals()[button] = True
    handleButtonPressEvent()


buttons = "BUTTON_X BUTTON_Y BUTTON_A BUTTON_B".split()

registerButtons(buttons)

actor = Actor()
inputHandler = InputHandler()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('button',
                        metavar='BUTTON', choices=buttons, nargs='?',
                        help="Press one of the X, Y, A, B buttons")

    pressed = parser.parse_args()

    if pressed.button is not None:
        globals()[pressed.button] = True

    handleButtonPressEvent()
