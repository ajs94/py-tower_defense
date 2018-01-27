from invader_types import *
from tkinter import *
from random import *

class Wave:

    def __init__(self, canvas, path, invaders, wait):
        self._canv = canvas
        self._path = path

        self.invadersDict = invaders
        self.invaderTypeList = self.getInvaderTypes()

        self.invadersList = []
        self.numInvaders = self.getTotalNumInvaders()
        self.waveComplete = False

        self.waitTime = wait
        self.numInvadersSpawned = 0

        for i in range(0, len(self.invadersDict)):
            self.checkIfTypeLeft()

    def update(self):
        for invader in self.invadersList:
            if invader._offCanvas:
                self.invadersList.remove(invader)
                self.numInvaders = self.numInvaders - 1
        if self.numInvaders == 0:
            self.waveComplete = True

    def spawnInvader(self, count):
        if self.numInvadersSpawned < self.numInvaders:
            self.checkIfTypeLeft()
            self.invadersList.append(self.getNextInvader())
            self.numInvadersSpawned = count + 1
            self._canv.after(self.waitTime, self.spawnInvader, self.numInvadersSpawned)

    # make into a factory later?
    def getNextInvader(self):
        nextType = choice(self.invaderTypeList)

        if nextType == 'goblin':
            self.invadersDict[nextType] -= 1
            return Goblin(self._canv, self._path)
        elif nextType == 'troll':
            self.invadersDict[nextType] -= 1
            return Troll(self._canv, self._path)
        elif nextType == 'orc':
            self.invadersDict[nextType] -= 1
            return Orc(self._canv, self._path)
        elif nextType == 'ogre':
            self.invadersDict[nextType] -= 1
            return Ogre(self._canv, self._path)
        elif nextType == 'dragon':
            self.invadersDict[nextType] -= 1
            return Dragon(self._canv, self._path)
        else:
            print('Wave complete')

    def checkIfTypeLeft(self):
        for key in self.invadersDict:
            if self.invadersDict[key] <= 0:
                del self.invadersDict[key]
                self.invaderTypeList = self.getInvaderTypes()
                break

    def getInvaderTypes(self):
        invaderTypes = []
        for key in self.invadersDict.keys():
            invaderTypes.append(key)
        return invaderTypes

    def getTotalNumInvaders(self):
        total = 0
        for key in self.invadersDict.keys():
            total += self.invadersDict.get(key)
        return total
