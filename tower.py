

class Tower:

    BASE_TOWER_TYPES = {'red': 'red', 'blue': 'blue', 'yellow': 'yellow'}
    UPGRADED_TOWER_TYPES = {'orange': 'orange', 'purple': 'purple', 'green': 'green'}

    # make these their own class?
    @staticmethod
    def createBaseTower(tower_type, canvas, waveList, col, row):
        if tower_type == "red":
            from tower_factory import RedTowerFactory
            factory = RedTowerFactory()
        elif tower_type == "blue":
            from tower_factory import BlueTowerFactory
            factory = BlueTowerFactory()
        elif tower_type == "yellow":
            from tower_factory import YellowTowerFactory
            factory = YellowTowerFactory()
        else:
            return
        return factory.makeTowerColor(canvas, waveList, col, row)

    @staticmethod
    def createUpgradedTower(existing_tower, new_tower, canvas, waveList, col, row):
        if (existing_tower == "red" and new_tower == "yellow") or (existing_tower == "yellow" and new_tower == "red"):
            from tower_factory import OrangeTowerFactory
            factory = OrangeTowerFactory()
        elif (existing_tower == "red" and new_tower == "blue") or (existing_tower == "blue" and new_tower == "red"):
            from tower_factory import PurpleTowerFactory
            factory = PurpleTowerFactory()
        elif (existing_tower == "yellow" and new_tower == "blue") or (existing_tower == "blue" and new_tower == "yellow"):
            from tower_factory import GreenTowerFactory
            factory = GreenTowerFactory()
        else:
            return
        return factory.makeTowerColor(canvas, waveList, col, row)

    def __init__(self, canvas, waveList, col, row):
        self._canv = canvas
        self._waveList = waveList
        self._shootingRange = 2
        self.fireSpeed = 500

        self.cooldownFlag = False
        self.currentTarget = None
        self._onCanvas = True

        self._x = row
        self._y = col
        self.update(waveList)

    def update(self, waveList):
        if self._onCanvas:
            self.cooldownFlag = False
            if self.currentTarget is not None and self.isInRange(self.currentTarget):
                if self.currentTarget._offCanvas == False:
                    self.shoot(self.currentTarget)
                else:
                    self.currentTarget = None
                    self.findNewTarget(waveList)
            else:
                self.findNewTarget(waveList)
            self._canv.after(self.fireSpeed, self.update, waveList)

    def findNewTarget(self, waveList):
        if self.cooldownFlag == False:
            for wave in waveList:
                for invader in wave.invadersList:
                    if self.isInRange(invader):
                        self.currentTarget = invader
                        self.shoot(self.currentTarget)
                        break

    # TODO: Change 30 to the size of a tile variable?
    def isInRange(self, target):
        distance = ((abs(target._x / 30) - self._x) ** 2) + ((abs(target._y / 30) - self._y) ** 2)
        if distance <= (self._shootingRange ** 2)+1:
            return True
        else:
            self.currentTarget = None
            return False

    def drawTower(self):
        print("test")

    def shoot(self, target):
        self.cooldownFlag = True
        self.currentTarget = target

