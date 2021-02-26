from Organizmy.POLOZENIE import POLOZENIE
from Organizmy.Rosliny.roslina import Roslina


class WilczeJagody(Roslina):
    __name = "JAG"

    def __init__(self, xswiat,  xsila = 99,  xinicjatywa = 0,  xwsp = POLOZENIE(0,0),  xwiek = 0):
        super().__init__(xswiat, xsila, xinicjatywa, xwsp, xwiek)
        self.setKolor((22, 54, 160))


    def rysowanie(self):
        return self.__name

    def dodaj(self, wsp):
        self._swiat.dodajOrganizm(WilczeJagody(self._swiat, xwsp=wsp), wsp)

    def kolizja(self,atakujacy):
        atakujacy.setIstnieje(False)
        self._swiat.dodajOrganizm(None, atakujacy.getWsp())
        temp = atakujacy.rysowanie() + " zjadl " + self.rysowanie() + " i umarl \n"
        self._swiat.setKomunikat(temp)

