from Organizmy.POLOZENIE import POLOZENIE
from tile import Tile


class Plansza:

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._plansza = [[None for x in range(self._height)] for y in range(self._width)]
        for x in range(0, self._width):
            for y in range(0, self._height):
                self._plansza[x][y] = Tile(POLOZENIE(x, y), None)


    def getPlansza(self):
        return self._plansza

    def setPlansza(self,plansza):
         self._plansza = plansza

    def getTile(self, x, y):
        return self._plansza[x][y]


