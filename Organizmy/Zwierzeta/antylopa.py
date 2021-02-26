from Organizmy.POLOZENIE import POLOZENIE
from Organizmy.Zwierzeta.zwierze import Zwierze
import random
from Organizmy.KIERUNEK import KIERUNEK

class Antylopa(Zwierze):
    __name = "AN"
    def __init__(self, xswiat,  xsila = 4,  xinicjatywa = 4,  xwsp = POLOZENIE(0,0),  xwiek = 0):
        super().__init__(xswiat, xsila, xinicjatywa, xwsp, xwiek)
        self.setKolor((132, 86, 7))
        self.setZasieg(2)


    def rysowanie(self):
        return self.__name

    def dodaj(self, wsp):
        self._swiat.dodajOrganizm(Antylopa(self._swiat, xwsp=wsp), wsp)

    def kolizja(self, atakujacy):
        rand = random.randint(0,100)

        if self.rysowanie() == atakujacy.rysowanie():
            gdzie = self.losujKierunek(self, 1)
            self.rozmnoz(gdzie)
            atakujacy.setRozmnozone(True)
            temp = self.rysowanie() + " rozmnozyly sie. \n"
            self._swiat.setKomunikat(temp)

        elif rand < 50:
            licznik = 0
            gora = 0
            dol = 0
            lewo = 0
            prawo = 0
            while licznik < 4:
                gdzie = self.losujKierunek(self,self.getZasieg())
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

                if self.czyWolne(gdzie,1) or \
                        (licznik == 2 and ((self.getWsp().x == 0 and self.getWsp().y == 0) or \
                                           (self.getWsp().x == 0 and self.getWsp().y == self._swiat.getY() - 1) or \
                                           (self.getWsp().x == self._swiat.getX() - 1 and self.getWsp().y == 0) or \
                                           (
                                                   self.getWsp().x == self._swiat.getX() - 1 and self.getWsp().y == self._swiat.getY() - 1))) or \
                        (licznik == 3 and ((self.getWsp().y == 0) or (self.getWsp().y == self._swiat.getY() - 1) or \
                                           (self.getWsp().x == 0) or (self.getWsp().x == self._swiat.getX() - 1))):
                    break

            self.ucieknij(self, gdzie)
            temp = self.rysowanie() + " uciekla przed " + atakujacy.rysowanie() + "\n"
            self._swiat.setKomunikat(temp)

        else:
            super().kolizja(atakujacy)

    def ucieknij(self, org, gdzie):
        wsp1 = org.getWsp()
        wsp2 = POLOZENIE(wsp1.x, wsp1.y)

        if gdzie == KIERUNEK.GORA:
            wsp2.y -= 1
        elif gdzie == KIERUNEK.DOL:
            wsp2.y += 1
        elif gdzie == KIERUNEK.LEWO:
            wsp2.x -= 1
        elif gdzie == KIERUNEK.PRAWO:
            wsp2.x += 1

        org.setWsp(wsp2)
        self._swiat.dodajOrganizm(org,wsp2)
        self._swiat.dodajOrganizm(None,wsp1)







