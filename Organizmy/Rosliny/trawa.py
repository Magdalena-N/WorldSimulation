from Organizmy.POLOZENIE import POLOZENIE
from Organizmy.Rosliny.roslina import Roslina


class Trawa(Roslina):
    __name = "TR"

    def __init__(self, xswiat,  xsila = 0,  xinicjatywa = 0,  xwsp = POLOZENIE(0,0),  xwiek = 0):
        super().__init__(xswiat, xsila, xinicjatywa, xwsp, xwiek)
        self.setKolor((202, 255, 104))


    def rysowanie(self):
        return self.__name

    def dodaj(self, wsp):
        self._swiat.dodajOrganizm(Trawa(self._swiat, xwsp=wsp), wsp)

