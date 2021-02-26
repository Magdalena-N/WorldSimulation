from math import fabs

from Organizmy.POLOZENIE import POLOZENIE
from Organizmy.Rosliny.barszczsosnowskiego import BarszczSosnowskiego
from Organizmy.Zwierzeta.zwierze import Zwierze
from Organizmy.KIERUNEK import KIERUNEK


class Cyberowca(Zwierze):
    __name = "CO"
    __cel = POLOZENIE(-1, -1)

    def __init__(self, xswiat,  xsila = 11,  xinicjatywa = 4,  xwsp = POLOZENIE(0,0),  xwiek = 0):
        super().__init__(xswiat, xsila, xinicjatywa, xwsp, xwiek)
        self.setKolor((0, 255, 208))


    def rysowanie(self):
        return self.__name

    def dodaj(self, wsp):
        self._swiat.dodajOrganizm(Cyberowca(self._swiat, xwsp=wsp), wsp)

    def znajdzBarszcz(self):
        pozycja = self.getWsp()
        x = pozycja.x
        y = pozycja.y
        min = -1
        polozenie = POLOZENIE(-1, -1)

        for i in range(0, self._swiat.getY()):
            for j in range(0, self._swiat.getX()):
                if isinstance(self._swiat._plansza.getTile(j,i).get_organizm(), BarszczSosnowskiego):

                    min2 = fabs(j - x) + fabs(i - y)

                    if min2 < min or min == -1:
                        min = min2
                        polozenie.x = j
                        polozenie.y = i

        self.__cel = polozenie

    def akcja(self):

        self.znajdzBarszcz()
        if self.__cel.x == -1 and self.__cel.y == -1:
            super().akcja()

        else:

            dx = fabs(self.__cel.x - self.getWsp().x)
            dy = fabs(self.__cel.y - self.getWsp().y)
            if dx > dy:
                if self.__cel.x > self.getWsp().x:
                    gdzie = KIERUNEK.PRAWO
                else:
                    gdzie = KIERUNEK.LEWO
            else:
                if self.__cel.y < self.getWsp().y:
                    gdzie = KIERUNEK.GORA
                else:
                    gdzie = KIERUNEK.DOL

            if (dx <= 1 and dy == 0) or (dx == 0 and dy <= 1):
                self._swiat._plansza.getTile(self.__cel.x, self.__cel.y).get_organizm().setIstnieje(False)
            self.ruch(self, gdzie)


