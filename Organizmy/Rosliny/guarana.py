from Organizmy.POLOZENIE import POLOZENIE
from Organizmy.Rosliny.roslina import Roslina


class Guarana(Roslina):
    __name = "GU"

    def __init__(self, xswiat,  xsila = 0,  xinicjatywa = 0,  xwsp = POLOZENIE(0,0),  xwiek = 0):
        super().__init__(xswiat, xsila, xinicjatywa, xwsp, xwiek)
        self.setKolor((255, 38, 0))


    def rysowanie(self):
        return self.__name

    def dodaj(self, wsp):
        self._swiat.dodajOrganizm(Guarana(self._swiat, xwsp=wsp), wsp)

    def kolizja(self,atakujacy):
        super().kolizja(atakujacy)
        atakujacy.setSila(atakujacy.getSila() + 3)

