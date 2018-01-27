from abc import ABC, abstractmethod

class Invader:

    INVADER_TYPES = {'goblin': 'green', 'troll': 'grey', 'orc': 'green', 'ogre': 'tan', 'dragon': 'red'}

    def __init__(self, canvas, path):
        self._canv = canvas
        self._path = path

        self._health = 100
        self._size = 4   # radius of circle to draw (for now)
        self._speed = 2

        self._reachedGoal = False
        self._offCanvas = False

        # _dest_cell is the next cell's center that we are moving toward.
        # Start at the 0th cell, which may be off the screen.  Use it
        # to get your x, y value.  Then, find the 1st cell and use that to
        # set the x and y directions.
        self._dest_cell_idx = 0
        self._dest_cell = self._path.get_cell(0)
        self._x, self._y = self._dest_cell.get_center()

        self._compute_new_dir()

        # identifier for the circle we draw to represent the invader
        self._id = None

    def update(self):
        if(self._x, self._y) == self._path._pathGoal.get_center():
            self._reachedGoal = True
            self.remove()
        elif self._health >= 0:
            self.render()
        else:
            self.remove()

    def _compute_new_dir(self):
        '''Get (and remember) the next cell in that path, and then
        compute the xdir and ydir to get us from our current position
        to the center of that next cell.'''
        self._dest_cell_idx += 1
        self._dest_cell = self._path.get_cell(self._dest_cell_idx)
        d = self._dest_cell.get_center_x() - self._x
        if d > 0:
            self._xdir = self._speed
        elif d == 0:
            self._xdir = 0
        else:
            self._xdir = -self._speed
        d = self._dest_cell.get_center_y() - self._y
        if d > 0:
            self._ydir = self._speed
        elif d == 0:
            self._ydir = 0
        else:
            self._ydir = -self._speed

    def move(self):
        if (self._x, self._y) == self._dest_cell.get_center():
            self._compute_new_dir()
        self._x += self._xdir
        self._y += self._ydir

    @abstractmethod
    def render(self):
        self._canv.delete(self._id)
        self.move()
        self._id = self._canv.create_oval(self._x - self._size, self._y - self._size,
                                          self._x + self._size, self._y + self._size,
                                          fill="black")

    def remove(self):
        self._canv.delete(self._id)
        self._offCanvas = True
