from Organizmy.POLOZENIE import POLOZENIE
from Organizmy.Zwierzeta.zwierze import Zwierze
from Organizmy.KIERUNEK import KIERUNEK

class Lis(Zwierze):
    __name = "L"
    def __init__(self, xswiat,  xsila = 3,  xinicjatywa = 7,  xwsp = POLOZENIE(0,0),  xwiek = 0):
        super().__init__(xswiat, xsila, xinicjatywa, xwsp, xwiek)
        self.setKolor((232, 147, 2))


    def rysowanie(self):
        return self.__name

    def dodaj(self, wsp):
        self._swiat.dodajOrganizm(Lis(self._swiat, xwsp=wsp), wsp)

    def akcja(self):
        szukaj = 1
        licznik = 0
        gora = 0
        dol = 0
        lewo = 0
        prawo = 0
        while licznik < 4:
            gdzie = self.losujKierunek(self,1)
            wsp2 = POLOZENIE(self.getWsp().x,self.getWsp().y)
            x = wsp2.x
            y = wsp2.y
            if gdzie == KIERUNEK.GORA:
                y -= 1
            elif gdzie == KIERUNEK.DOL:
                y += 1
            elif gdzie == KIERUNEK.LEWO:
                x -= 1
            elif gdzie == KIERUNEK.PRAWO:
                x += 1

            if self.czyWolne(gdzie, self.getZasieg()):
                self.ruch(self,gdzie)
                szukaj = 0
            else:
                wsp2.x = x
                wsp2.y = y
                org = self._swiat.getOrganizm(wsp2)
                if org.getSila() <= self.getSila():
                    szukaj = 0
                    self._swiat.getOrganizm(wsp2).kolizja(self)
                    if not self._swiat.getOrganizm(self.getWsp()) is None and \
                        self.getOdbity() is False:
                        self.ruch(self,gdzie)
                    elif not self._swiat.getOrganizm(self.getWsp()) is None and \
                        self.getOdbity() is True:
                        self.setOdbity(False)
                else:
                    if gora == 0 and gdzie == KIERUNEK.GORA:
                        gora = 1
                        licznik += 1
                    elif dol == 0 and gdzie == KIERUNEK.DOL:
                        dol = 1
                        licznik += 1
                    elif lewo == 0 and gdzie == KIERUNEK.LEWO:
                        lewo = 1
                        licznik += 1
                    elif prawo == 0 and gdzie == KIERUNEK.PRAWO:
                        prawo = 1
                        licznik += 1

            if szukaj == 0 or licznik == 4 or \
                    (licznik == 2 and ((self.getWsp().x == 0 and self.getWsp().y == 0) or \
                                       (self.getWsp().x == 0 and self.getWsp().y == self._swiat.getY() - 1) or \
                                       (self.getWsp().x == self._swiat.getX() - 1 and self.getWsp().y == 0) or \
                                       (self.getWsp().x == self._swiat.getX() - 1 and self.getWsp().y == self._swiat.getY() - 1))) or \
                    (licznik == 3 and (( self.getWsp().y == 0 ) or ( self.getWsp().y == self._swiat.getY()- 1 ) or \
                                       ( self.getWsp().x == 0 ) or ( self. getWsp().x == self._swiat.getX() - 1))):
                break
