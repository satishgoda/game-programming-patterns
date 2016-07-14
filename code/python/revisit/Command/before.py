from actions import jump, fireGun, swapWeapon, lurchIneffectively

from keys import BUTTON_X, BUTTON_Y, BUTTON_A, BUTTON_B


class InputHandler(object):

    def handleInput(self):
        if isPressed(BUTTON_X):
            jump()
        elif isPressed(BUTTON_Y):
            fireGun()
        elif isPressed(BUTTON_A):
            swapWeapon()
        elif isPressed(BUTTON_B):
            lurchIneffectively()
