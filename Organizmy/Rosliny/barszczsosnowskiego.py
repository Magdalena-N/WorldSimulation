from Organizmy.POLOZENIE import POLOZENIE
from Organizmy.Rosliny.roslina import Roslina
from Organizmy.KIERUNEK import KIERUNEK

class BarszczSosnowskiego(Roslina):
    __name = "BA"

    def __init__(self, xswiat,  xsila = 10,  xinicjatywa = 0,  xwsp = POLOZENIE(0,0),  xwiek = 0):
        super().__init__(xswiat, xsila, xinicjatywa, xwsp, xwiek)
        self.setKolor((137, 13, 59))

    def rysowanie(self):
        return self.__name

    def dodaj(self, wsp):
        self._swiat.dodajOrganizm(BarszczSosnowskiego(self._swiat, xwsp=wsp), wsp)


    def kolizja(self,atakujacy):
        if atakujacy.rysowanie() == "CO":
            self.setIstnieje(False)
            self._swiat.dodajOrganizm(None, self.getWsp())
            temp = self.rysowanie() + " dopadla cyberowca \n"
            self._swiat.setKomunikat(temp)
        else:
            atakujacy.setIstnieje(False)
            self._swiat.dodajOrganizm(None, atakujacy.getWsp())
            temp = atakujacy.rysowanie() + " zjadl " + self.rysowanie() + " i umarl \n"
            self._swiat.setKomunikat(temp)

    def akcja(self):
        pozycja = self.getWsp()
        pozycja2 = POLOZENIE(pozycja.x, pozycja.y)

        if pozycja.y != 0 and self.czyWolne(KIERUNEK.GORA) is False:
            pozycja2.y -= 1
            if self._swiat.getOrganizm(pozycja2).rysowanie() != self.rysowanie() and \
                    self._swiat.getOrganizm(pozycja2).rysowanie() != "CO":
                self._swiat.getOrganizm(pozycja2).setIstnieje(False)
                self._swiat.dodajOrganizm(None, pozycja2)
            pozycja2.y += 1

        if pozycja.y != self._swiat.getY() - 1 and self.czyWolne(KIERUNEK.DOL) is False:
            pozycja2.y += 1
            if self._swiat.getOrganizm(pozycja2).rysowanie() != self.rysowanie() and \
                    self._swiat.getOrganizm(pozycja2).rysowanie() != "CO":
                self._swiat.getOrganizm(pozycja2).setIstnieje(False)
                self._swiat.dodajOrganizm(None, pozycja2)
            pozycja2.y -= 1

        if pozycja.x != 0 and self.czyWolne(KIERUNEK.LEWO) is False:
            pozycja2.x -= 1
            if self._swiat.getOrganizm(pozycja2).rysowanie() != self.rysowanie() and \
                    self._swiat.getOrganizm(pozycja2).rysowanie() != "CO":
                self._swiat.getOrganizm(pozycja2).setIstnieje(False)
                self._swiat.dodajOrganizm(None, pozycja2)

            pozycja2.x += 1

        if pozycja.x != self._swiat.getX() - 1 and self.czyWolne(KIERUNEK.PRAWO) is False:
            pozycja2.x += 1
            if self._swiat.getOrganizm(pozycja2).rysowanie() != self.rysowanie() and \
                    self._swiat.getOrganizm(pozycja2).rysowanie() != "CO":
                self._swiat.getOrganizm(pozycja2).setIstnieje(False)
                self._swiat.dodajOrganizm(None, pozycja2)

            pozycja2.x -= 1

        super().akcja()

