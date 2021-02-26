from Organizmy.POLOZENIE import POLOZENIE
from Organizmy.Zwierzeta.zwierze import Zwierze


class Wilk(Zwierze):
    __name = "W"
    def __init__(self, xswiat,  xsila = 9,  xinicjatywa = 5,  xwsp = POLOZENIE(0,0),  xwiek = 0):
        super().__init__(xswiat, xsila, xinicjatywa, xwsp, xwiek)
        self.setKolor((132, 132, 132))


    def rysowanie(self):
        return self.__name

    def dodaj(self, wsp):
        self._swiat.dodajOrganizm(Wilk(self._swiat, xwsp=wsp), wsp)

