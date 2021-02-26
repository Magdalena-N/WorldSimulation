from Organizmy.POLOZENIE import POLOZENIE
from Organizmy.Rosliny.roslina import Roslina


class Mlecz(Roslina):
    __name = "ML"

    def __init__(self, xswiat,  xsila = 0,  xinicjatywa = 0,  xwsp = POLOZENIE(0,0),  xwiek = 0):
        super().__init__(xswiat, xsila, xinicjatywa, xwsp, xwiek)
        self.setKolor((255, 246, 0))


    def rysowanie(self):
        return self.__name

    def dodaj(self, wsp):
        self._swiat.dodajOrganizm(Mlecz(self._swiat, xwsp=wsp), wsp)

    def akcja(self):
        for i in range(0,3):
            super().akcja()

