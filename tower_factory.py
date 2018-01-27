from tower_types import *


class TowerFactory:

    def makeTowerColor(self, canvas, waveList, col, row):
        pass

    def makeTower(self, canvas, waveList, col, row):
        tower = self.makeTowerColor(canvas, waveList, col, row)
        return tower


''' The Base Tower Types: created on empty tiles'''

class RedTowerFactory(TowerFactory):

    def makeTowerColor(self, canvas, waveList, col, row):
        return RedTower(canvas, waveList, col, row)


class BlueTowerFactory(TowerFactory):

    def makeTowerColor(self, canvas, waveList, col, row):
        return BlueTower(canvas, waveList, col, row)


class YellowTowerFactory(TowerFactory):

    def makeTowerColor(self, canvas, waveList, col, row):
        return YellowTower(canvas, waveList, col, row)


''' The combination tower types: created by clicking on existing towers'''


class OrangeTowerFactory(TowerFactory):

    def makeTowerColor(self, canvas, waveList, col, row):
        return OrangeTower(canvas, waveList, col, row)


class PurpleTowerFactory(TowerFactory):

    def makeTowerColor(self, canvas, waveList, col, row):
        return PurpleTower(canvas, waveList, col, row)


class GreenTowerFactory(TowerFactory):

    def makeTowerColor(self, canvas, waveList, col, row):
        return GreenTower(canvas, waveList, col, row)