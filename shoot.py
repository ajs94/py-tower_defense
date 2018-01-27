from random import *


class Shoot:

    def __init__(self, canvas, x, y, target):
        self._canv = canvas
        self._x = x
        self._y = y
        self._target = target
        self._color = "black"
        self._damage = 1
        self._line = None
        self._offset = 5

    def render(self):
        self.remove()

        if self._offset >= -5:
            self._line = self._canv.create_line(self._x * 30 + 15 + randint(0, 5), self._y * 30 + 5 + randint(0, 5),
                                                self._target._x + self._offset, self._target._y + self._offset,
                                                dash=abs(self._offset), fill=self._color, width=5.0 - self._offset)
            self._offset = self._offset - 2
            self.effect()
            self._canv.after(30, self.render)

    def remove(self):
        self._canv.delete(self._line)

    def effect(self):
        self._target._health = self._target._health - self._damage