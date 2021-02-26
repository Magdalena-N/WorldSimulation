from Organizmy.POLOZENIE import POLOZENIE
from Organizmy.Zwierzeta.zwierze import Zwierze

class Owca(Zwierze):
    __name = "OW"

    def __init__(self, xswiat,  xsila = 4,  xinicjatywa = 4,  xwsp = POLOZENIE(0,0),  xwiek = 0):
        super().__init__(xswiat, xsila, xinicjatywa, xwsp, xwiek)
        self.setKolor((190, 205, 229))

    def rysowanie(self):
        return self.__name

    def dodaj(self, wsp):
        self._swiat.dodajOrganizm(Owca(self._swiat, xwsp=wsp), wsp)


