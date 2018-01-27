from tower import *
from shoot_factory import *


''' The Base Tower Types: created on empty tiles'''


class RedTower(Tower):

    def __init__(self, canvas, waveList, col, row):
        Tower.__init__(self, canvas, waveList, col, row)

    def shoot(self, target):
        ShootFactory.factory("red", self._canv, self._x, self._y, target)
        self.cooldownFlag = True
        self.currentTarget = target


class BlueTower(Tower):

    def __init__(self, canvas, waveList, col, row):
        Tower.__init__(self, canvas, waveList, col, row)
        self._color = "blue"
        self._shootingRange = 4

    def shoot(self, target):
        ShootFactory.factory("blue", self._canv, self._x, self._y, target)
        self.cooldownFlag = True
        self.currentTarget = target

class YellowTower(Tower):

    def __init__(self, canvas, waveList, col, row):
        Tower.__init__(self, canvas, waveList, col, row)
        self.fireSpeed = 250

    def shoot(self, target):
        ShootFactory.factory("yellow", self._canv, self._x, self._y, target)
        self.cooldownFlag = True
        self.currentTarget = target



''' The combination tower types: created by clicking on existing towers'''


class OrangeTower(Tower):

    def __init__(self, canvas, waveList, col, row):
        Tower.__init__(self, canvas, waveList, col, row)
        self._color = "orange"
        self.fireSpeed = 250

    def shoot(self, target):
        ShootFactory.factory("orange", self._canv, self._x, self._y, target)
        self.cooldownFlag = True
        self.currentTarget = target


class PurpleTower(Tower):

    def __init__(self, canvas, waveList, col, row):
        Tower.__init__(self, canvas, waveList, col, row)
        self._color = "purple"
        self._shootingRange = 4

    def shoot(self, target):
        ShootFactory.factory("purple", self._canv, self._x, self._y, target)
        self.cooldownFlag = True
        self.currentTarget = target


class GreenTower(Tower):

    def __init__(self, canvas, waveList, col, row):
        Tower.__init__(self, canvas, waveList, col, row)
        self._color = "green"
        self._shootingRange = 4
        self.fireSpeed = 250

    def shoot(self, target):
        ShootFactory.factory("green", self._canv, self._x, self._y, target)
        self.cooldownFlag = True
        self.currentTarget = target