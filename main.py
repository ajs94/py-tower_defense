from tkinter import *
from time import *

from path import *
from wave import *
from tower import *

CANVAS_DIM = 600
SQUARE_SIZE = 30
NUM_CELLS_PER_DIM = int(CANVAS_DIM / SQUARE_SIZE)

TIME_BETWEEN_WAVES = 120    # seconds
INIT_GOLD_AMOUNT = 100
INIT_NUM_LIVES = 5

class App:
    def __init__(self, root):

        self._root = root
        self._gameRunning = False

        self._currWaveNumber = 0
        self._currWave = None
        self._livesLeft = INIT_NUM_LIVES
        self._goldLeft = INIT_GOLD_AMOUNT
        self._totalScore = 0

        # A list of the towers
        self.towerList = []
        self.towerTypeList = self.getTowerTypes()
        self.nextTower = self.getNextTower()

        self.createGUI()

        # A 2-d grid of locations
        self.createGrid()

        # A list of waves
        self.waveList = []
        self.waveNumber = 0

        # Follow the mouse everywhere and highlight the cell it is in.
        # self._canv.bind("<Motion>", self.highlight_cell)

        self.readPathInfo()
        self.readWaveInfo()

        self.update()

    def update(self):
        for wave in self.waveList:
            for invader in wave.invadersList:
                invader.update()
                if invader._offCanvas:
                    self._goldLeft += 10
                    self._totalScore += 10
                    self._goldAmtVar.set(self._goldLeft)
                    wave.update()
                if invader._reachedGoal:
                    self._livesLeft = self._livesLeft - 1
                    wave.update()
                    self._livesLeftVariable.set(self._livesLeft)
                    break
        if self._livesLeft <= 0:
            self.gameOver()

        self._canv.after(30, self.update)

    def createGUI(self):

        self._bottom_panel = Frame(root)
        self._bottom_panel.pack(side=RIGHT)

        self._canv = Canvas(root, width=CANVAS_DIM, height=CANVAS_DIM)
        self._canv.pack()

        self._canv.bind("<Button-1>", self.setTower)

        Label(self._bottom_panel, text="Next tower: ").grid(row=0, column=0)
        self._towerTypeVariable = StringVar()
        self._towerTypeVariable.set(self.nextTower)
        self._nextTowerLabel = Label(self._bottom_panel, textvariable=self._towerTypeVariable)
        self._nextTowerLabel.grid(row=0, column=1)

        Label(self._bottom_panel, text="Lives left: ").grid(row=1, column=0)
        self._livesLeftVariable = StringVar()
        self._livesLeftVariable.set(self._livesLeft)
        self._livesLeftLabel = Label(self._bottom_panel, textvariable=self._livesLeftVariable)
        self._livesLeftLabel.grid(row=1, column=1)

        Label(self._bottom_panel, text="Gold: ").grid(row=2, column=0)
        self._goldAmtVar = IntVar()
        self._goldAmtVar.set(self._goldLeft)
        self._goldLbl = Label(self._bottom_panel, textvariable=self._goldAmtVar)
        self._goldLbl.grid(row=2, column=1)

        Label(self._bottom_panel, text="Time: ").grid(row=3, column=0)
        self._timeLeftTilWave = IntVar()
        self._timeLeftTilWave.set(TIME_BETWEEN_WAVES)
        self._timeLeftLbl = Label(self._bottom_panel, textvariable=self._timeLeftTilWave)
        self._timeLeftLbl.grid(row=3, column=1)

        # Buttons
        self._btStartGame = Button(self._bottom_panel, background='grey', text="Start Game",
                                   command=self.startGame)
        self._btStartGame.grid(row=4, column=0, pady=100)

        self._btNextWave = Button(self._bottom_panel, background='grey', text="Start Wave",
                                  command=self.startNextWave)
        self._btNextWave.grid(row=4, column=1, pady=100)

    def createGrid(self):
        self._grid = []
        for row in range(NUM_CELLS_PER_DIM):
            rowlist = []
            for col in range(NUM_CELLS_PER_DIM):
                cell = Cell(self._canv, col, row, SQUARE_SIZE)
                rowlist.append(cell)
            self._grid.append(rowlist)

    def highlight_cell(self, event):
        '''Highlight the cell the mouse is over.'''
        if not self._gameRunning:
            return
        x, y = event.x, event.y
        for row in range(NUM_CELLS_PER_DIM):
            for col in range(NUM_CELLS_PER_DIM):
                if (x, y) in self._grid[col][row]:
                    self._grid[col][row].render()


    def startGame(self):
        if self._gameRunning:
            print("Game in progress...")
            return
        self._gameRunning = True
        self.waveList[0].spawnInvader(0)
        self.waveNumber = self.waveNumber + 1
        print("Starting game...")
        # Start the timer, which forces the next wave to start in a few seconds.
        self.updateTimer()

    def startNextWave(self):
        '''Start the next wave now, instead of waiting for the timer to go down to 0.'''
        if not self._gameRunning:
            return
        self.waveList[self.waveNumber].spawnInvader(0)
        self.waveNumber = self.waveNumber + 1
        print("Start next wave now...")
        self._timeLeftTilWave.set(TIME_BETWEEN_WAVES)

    def updateTimer(self):
        timeLeft = self._timeLeftTilWave.get()
        timeLeft -= 1
        self._timeLeftTilWave.set(timeLeft)
        if timeLeft == 0:
            pass
        self._canv.after(1000, self.updateTimer)

    def updateGold(self):
        self._goldAmtVar.set(self._goldLeft)

    def readPathInfo(self):
        '''Read path information from a file and create a path object for it.'''
        self._path = Path(NUM_CELLS_PER_DIM)
        with open('path.txt') as pf:
            for elem in pf:
                elem = elem.strip()
                x, y = map(int, elem.split(','))   # map(int) to make ints.
                self._path.add_cell(self._grid[y][x])
                self._grid[y][x].set_type('path')


    def readWaveInfo(self):
        with open('wave.txt') as pf:
            for elem in pf:
                elem = elem.strip()
                goblins, trolls, orcs, ogres, dragons, wait = map(int, elem.split(','))
                self.waveList.append(Wave(self._canv, self._path, {'goblin': goblins, 'troll': trolls,
                                                                   'orc': orcs, 'ogre': ogres, 'dragon': dragons}, wait))
        self._currWave = self.waveList[0]

    # refactor this later so it's not an eyesore
    def setTower(self, event):
        x, y = event.x, event.y
        for row in range(NUM_CELLS_PER_DIM):
            for col in range(NUM_CELLS_PER_DIM):
                if (x, y) in self._grid[col][row]:
                    if self._grid[col][row].get_type() != 'path':
                        if not self._grid[col][row].get_type() in Tower.BASE_TOWER_TYPES and not self._grid[col][row].get_type() in Tower.UPGRADED_TOWER_TYPES:
                            if self._goldLeft - 20 < 0:
                                print("Not enough gold")
                                return
                            self._goldLeft -= 20
                            self.updateGold()
                            self._grid[col][row].set_type(self.nextTower)
                            self.towerList.append(Tower.createBaseTower(self.nextTower, self._canv, self.waveList, col, row))
                            self.nextTower = self.getNextTower()
                            self._towerTypeVariable.set(self.nextTower)
                            break
                        elif self._grid[col][row].get_type() != self.nextTower and not self._grid[col][row].get_type() in Tower.UPGRADED_TOWER_TYPES:
                            if self._goldLeft - 40 < 0:
                                print("Not enough gold")
                                return
                            for tower in self.towerList:
                                if tower._x == row and tower._y == col:
                                    self.towerList.remove(tower)
                                    # NOTE: this isn't deleting the tower object yet?
                                    tower._onCanvas = False
                            self._goldLeft -= 40
                            self.updateGold()
                            newTower = Tower.createUpgradedTower(self._grid[col][row].get_type(),
                                                                self.nextTower, self._canv, self.waveList,
                                                                col, row)
                            self.towerList.append(newTower)
                            self._grid[col][row].set_type(newTower._color)
                            self.nextTower = self.getNextTower()
                            self._towerTypeVariable.set(self.nextTower)
                            break



    def getTowerTypes(self):
        towerTypes = []
        for key in Tower.BASE_TOWER_TYPES.keys():
            towerTypes.append(key)
        return towerTypes

    def getNextTower(self):
        return choice(self.towerTypeList)

    def gameOver(self):
        print('Score: ', self._totalScore, '\nGame Over')
        sys.exit(30)


root = Tk()
root.title("Calvin Tower Defense")
App(root)
root.mainloop()

