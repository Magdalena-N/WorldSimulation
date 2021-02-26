from Organizmy.POLOZENIE import POLOZENIE
from Organizmy.Zwierzeta.zwierze import Zwierze
import random

class Zolw(Zwierze):
    __name = "ZO"
    def __init__(self, xswiat,  xsila = 2,  xinicjatywa = 1,  xwsp = POLOZENIE(0,0),  xwiek = 0):
        super().__init__(xswiat, xsila, xinicjatywa, xwsp, xwiek)
        self.setKolor((44, 140, 0))


    def rysowanie(self):
        return self.__name

    def dodaj(self, wsp):
        self._swiat.dodajOrganizm(Zolw(self._swiat, xwsp=wsp), wsp)

    def czyOdbilAtak(self, atakujacy):
        if self.rysowanie() == atakujacy.rysowanie():
            return False
        if atakujacy.getSila() < 5:
            return True
        else:
            return False

    def akcja(self):
        temp = random.randint(0, 100)
        if temp < 25:
            super().akcja()

    def kolizja(self, atakujacy):
        if self.czyOdbilAtak(atakujacy):
            temp = self.rysowanie() + " odbil atak " + atakujacy.rysowanie() + "\n"
            self._swiat.setKomunikat(temp)
            atakujacy.setOdbity(True)
        else:
            super().kolizja(atakujacy)

