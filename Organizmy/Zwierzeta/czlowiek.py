from Organizmy.POLOZENIE import POLOZENIE
from Organizmy.Zwierzeta.zwierze import Zwierze


class Czlowiek(Zwierze):
    __name = "?"

    def __init__(self,xswiat, xsila = 5, xinicjatywa = 4, xwsp = POLOZENIE(0,0), xwiek = 0):
        super().__init__(xswiat,xsila,xinicjatywa,xwsp,xwiek)
        self._swiat.setCzlowiekZyje(True)
        self.__czekaj = 0
        self.__pozostalyEliksir = 0
        self.setKolor((255, 211, 254))

    def akcja(self):
        if self.getUmiejetnosc() is True:
            self.uzyjUmiejetnosci()
            self.setUmiejetnosc(False)
        super().akcja()
        if self.__czekaj != 0:
            self.__czekaj-=1
        if self.__pozostalyEliksir > 0:
            self.__pozostalyEliksir-=1
            self.setSila((self.getSila()-1))
            if self.__pozostalyEliksir == 0:
                self.__czekaj = 5
                temp = "Eliksir sie skonczyl\n"
                self._swiat.setKomunikat(temp)



    def kolizja(self, atakujacy):
        super().kolizja(atakujacy)

        if self._swiat.getOrganizm(self.getWsp()) is None:
            self._swiat.setCzlowiekZyje(False)

    def rysowanie(self):
        return self.__name

    def dodaj(self, wsp):
        self._swiat.dodajOrganizm(Czlowiek(self._swiat,wsp),wsp)

    def uzyjEliksiru(self):
        temp = "Czlowiek wypil eliksir\n"
        self._swiat.setKomunikat(temp)
        self.setSila(self.getSila() + 10)
        self.__pozostalyEliksir = 5

    def uzyjUmiejetnosci(self):
        if self.__czekaj == 0 and self.__pozostalyEliksir == 0:
            self.uzyjEliksiru()

    def getCzekaj(self):
        return self.__czekaj
    def setCzekaj(self,xczekaj):
        self.__czekaj = xczekaj
    def getPozostalyEliksir(self):
        return self.__pozostalyEliksir
    def setPozostalyEliksir(self,pozostalyEliksir):
        self.__pozostalyEliksir = pozostalyEliksir
