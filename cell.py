from tkinter import *
import random
from tower import *


class Cell:

    TYPE2COL = { 'path': 'gray', 'tower': 'black', 'other': 'black' }
    TYPE2COL.update(Tower.BASE_TOWER_TYPES)
    TYPE2COL.update(Tower.UPGRADED_TOWER_TYPES)

    def __init__(self, canvas, x, y, size, type='other'):
        self._canv = canvas
        self._x = x
        self._y = y
        self._size = size
        self._ulx = x * size          # upper-left x
        self._lrx = self._ulx + size  # lower-right x
        self._uly = y * size          # upper-left y
        self._lry = self._uly + size  # lower-right y
        self._tag = "cell" + str(x) + str(y)
        self._id = None
        # True when the mouse is in this cell.
        self._mouseIn = False
        self.set_type(type)
        self._id = self._canv.create_rectangle(self._ulx, self._uly, self._lrx, self._lry,
                                               fill=Cell.TYPE2COL[self._type], tag=self._tag)

        # self._img = PhotoImage(file='empty.png')
        # self._canv.create_image(self._x * 30 + 15, self._y * 30 + 15, image=self._img)

        self._canv.tag_bind(self._id, "<Enter>", self.highlight)
        self._canv.tag_bind(self._id, "<Leave>", self.clear)

    def clear(self, event=None):
        self._mouseIn = False
        self._canv.itemconfig(self._id, fill=Cell.TYPE2COL[self._type])

    def highlight(self, event=None):
        # Show green where the mouse is.
        self._canv.itemconfig(self._id, fill='green')
        self._mouseIn = True

    '''Return True if the given x,y tuple is in the rectangle, False otherwise.'''
    def __contains__(self, xy):
        x, y = xy
        return self._ulx < x < self._lrx and self._uly < y < self._lry

    def get_x(self):
        return self._x
    def get_y(self):
        return self._y

    def get_center(self):
        return (self.get_center_x(), self.get_center_y())

    def get_center_x(self):
        return self._ulx + (self._size / 2)
    def get_center_y(self):
        return self._uly + (self._size / 2)

    def get_type(self):
        return self._type

    def set_type(self, type):
        self._type = type     # should use sub-class?
        if self._type == "red":
            self._img=PhotoImage(file='red.png')
            self._canv.create_image(self._x*30+15, self._y*30+15, image=self._img)
        elif self._type == "yellow":
            self._img=PhotoImage(file='yellow.png')
            self._canv.create_image(self._x*30+15, self._y*30+15, image=self._img)
        elif self._type == "blue":
            self._img=PhotoImage(file='blue.png')
            self._canv.create_image(self._x*30+15, self._y*30+15, image=self._img)
        elif self._type == "path":
            self._img=PhotoImage(file='path.png')
            self._canv.create_image(self._x*30+15, self._y*30+15, image=self._img)
        elif self._type == "orange":
            self._img = PhotoImage(file='orange.png')
            self._canv.create_image(self._x * 30 + 15, self._y * 30 + 15, image=self._img)
        elif self._type == "purple":
            self._img = PhotoImage(file='purple.png')
            self._canv.create_image(self._x * 30 + 15, self._y * 30 + 15, image=self._img)
        elif self._type == "green":
            self._img = PhotoImage(file='green.png')
            self._canv.create_image(self._x * 30 + 15, self._y * 30 + 15, image=self._img)

        elif self._type == "other":
            self._img=PhotoImage(file='empty.png')
            self._canv.create_image(self._x*30+15, self._y*30+15, image=self._img)
        elif self._id is not None:
            self._img = None
            self._canv.itemconfig(self._id, fill=Cell.TYPE2COL[self._type])