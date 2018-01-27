from shoot import *


''' The Base Tower Types: created on empty tiles'''


class ShootFactory:

    def factory(color, canvas, x, y, target):
        if color == "red":
            return RedShot(canvas, x, y, target)
        elif color == "blue":
            return  BlueShot(canvas, x, y, target)
        elif color == "yellow":
            return YellowShot(canvas, x, y, target)
        elif color == "orange":
            return OrangeShot(canvas, x, y, target)
        elif color == "purple":
            return PurpleShot(canvas, x, y, target)
        elif color == "green":
            return GreenShot(canvas, x, y, target)


# Types of shots
class RedShot(Shoot):

    def __init__(self, canvas, x, y, target):
        Shoot.__init__(self, canvas, x, y, target)
        self._damage = 2
        self._color = "red"
        self.render()


class BlueShot(Shoot):

    def __init__(self, canvas, x, y, target):
        Shoot.__init__(self, canvas, x, y, target)
        self._color = "blue"
        self.render()

class YellowShot(Shoot):

    def __init__(self, canvas, x, y, target):
        Shoot.__init__(self, canvas, x, y, target)
        self._color = "yellow"
        self.render()


''' The combination tower types: created by clicking on existing towers'''


class OrangeShot(Shoot):

    def __init__(self, canvas, x, y, target):
        Shoot.__init__(self, canvas, x, y, target)
        self._damage = 2
        self._color = "orange"
        self.render()


class PurpleShot(Shoot):

    def __init__(self, canvas, x, y, target):
        Shoot.__init__(self, canvas, x, y, target)
        self._damage = 2
        self._color = "purple"
        self.render()


class GreenShot(Shoot):

    def __init__(self, canvas, x, y, target):
        Shoot.__init__(self, canvas, x, y, target)
        self._color = "green"
        self.render()