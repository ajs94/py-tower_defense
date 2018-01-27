from invader import *
from random import *


class Goblin(Invader):

    def __init__(self, canvas, path):
        self._drawOffset = randint(-5,5)
        Invader.__init__(self, canvas, path)

        self._health = 100
        self._size = 4
        self._speed = 1

    def render(self):
        self._canv.delete(self._id)
        self.move()
        self._id = self._canv.create_oval(self._x - self._drawOffset - self._size, self._y - self._drawOffset - self._size,
                                          self._x - self._drawOffset + self._size, self._y - self._drawOffset + self._size,
                                          fill="green")

class Troll(Invader):

    def __init__(self, canvas, path):
        self._drawOffset = randint(-5,5)
        Invader.__init__(self, canvas, path)

        self._health = 300
        self._size = 6
        self._speed = 1

    def render(self):
        self._canv.delete(self._id)
        self.move()
        self._id = self._canv.create_oval(self._x - self._drawOffset - self._size, self._y - self._drawOffset - self._size,
                                          self._x - self._drawOffset + self._size, self._y - self._drawOffset + self._size,
                                          fill="white")


class Orc(Invader):

    def __init__(self, canvas, path):
        self._drawOffset = randint(-5,5)
        Invader.__init__(self, canvas, path)

        self._health = 250
        self._size = 7
        self._speed = 2

    def render(self):
        self._canv.delete(self._id)
        self.move()
        self._id = self._canv.create_oval(self._x - self._drawOffset - self._size, self._y - self._drawOffset - self._size,
                                          self._x - self._drawOffset + self._size, self._y - self._drawOffset + self._size,
                                          fill="green")


class Ogre(Invader):

    def __init__(self, canvas, path):
        self._drawOffset = randint(-5,5)
        Invader.__init__(self, canvas, path)

        self._health = 2000
        self._size = 10
        self._speed = .5

    def render(self):
        self._canv.delete(self._id)
        self.move()
        self._id = self._canv.create_oval(self._x - self._drawOffset - self._size, self._y - self._drawOffset - self._size,
                                          self._x - self._drawOffset + self._size, self._y - self._drawOffset + self._size,
                                          fill="tan")


class Dragon(Invader):

    def __init__(self, canvas, path):
        Invader.__init__(self, canvas, path)

        self._health = 10000
        self._size = 12
        self._speed = 1

    def render(self):
        self._canv.delete(self._id)
        self.move()
        self._id = self._canv.create_oval(self._x - self._size, self._y - self._size,
                                          self._x + self._size, self._y + self._size,
                                          fill="red")