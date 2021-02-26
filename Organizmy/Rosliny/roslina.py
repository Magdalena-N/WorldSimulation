import random
from Organizmy.KIERUNEK import KIERUNEK
from Organizmy.POLOZENIE import POLOZENIE
from Organizmy.organizm import Organizm
from abc import ABC, abstractmethod


class Roslina (Organizm):

    def __init__(self, xswiat, xsila = 0, xinicjatywa = 0, xwsp = POLOZENIE(0,0), xwiek = 0):
        super().__init__(xswiat, xsila , xinicjatywa, xwsp, xwiek)

    def akcja(self):
        temp = random.randint(0,10)
        if temp < 4:
            gdzie = self.losujKierunek(self)
            self.zasiej(self, gdzie)

    def czyWolne(self,gdzie):
        pozycja = POLOZENIE(self.getWsp().x, self.getWsp().y)

        if gdzie == KIERUNEK.GORA:
            pozycja.y -= 1
        elif gdzie == KIERUNEK.DOL:
            pozycja.y += 1
        elif gdzie == KIERUNEK.LEWO:
            pozycja.x -= 1
        elif gdzie == KIERUNEK.PRAWO:
            pozycja.x += 1

        nowapozycja = POLOZENIE(pozycja.x, pozycja.y)

        if self._swiat.getOrganizm(nowapozycja) is None:
            return True
        else:
            return False

    def zasiej(self,xorg, gdzie):
        wsp2 = POLOZENIE(xorg.getWsp().x, xorg.getWsp().y)

        if gdzie == KIERUNEK.GORA:
            wsp2.y -= 1
        elif gdzie == KIERUNEK.DOL:
            wsp2.y += 1
        elif gdzie == KIERUNEK.LEWO:
            wsp2.x -= 1
        elif gdzie == KIERUNEK.PRAWO:
            wsp2.x += 1

        if 0 <= wsp2.x < self._swiat.getX() and \
            0 <= wsp2.y < self._swiat.getY():
            if self.czyWolne(gdzie):
                self.dodaj(wsp2)


    def losujKierunek(self, org):

        gdzie = KIERUNEK.BRAK
        obecna_pozycja = org.getWsp()

        #obiekt calkiem z lewej
        if obecna_pozycja.x == 0:
            #lewy gorny rog(PRAWO,DOL)
            if obecna_pozycja.y == 0 :
                temp = random.randint(0,1)
                if temp == 0:
                    gdzie = KIERUNEK.PRAWO
                elif temp == 1:
                    gdzie = KIERUNEK.DOL

            #lewy dolny rog (GORA,PRAWO)
            elif obecna_pozycja.y == self._swiat.getY() - 1 :
                temp = random.randint(0,1)
                if temp == 0:
                    gdzie = KIERUNEK.GORA
                elif temp == 1:
                    gdzie = KIERUNEK.PRAWO

            #tylko w lewo nie moze
            else:
                temp = random.randint(0,2)
                if temp == 0:
                    gdzie = KIERUNEK.GORA
                elif temp == 1:
                    gdzie = KIERUNEK.PRAWO
                elif temp == 2:
                    gdzie = KIERUNEK.DOL

        #obiekt calkiem z prawej
        elif obecna_pozycja.x == self._swiat.getX() - 1 :
            #prawy gorny rog
            if obecna_pozycja.y == 0 :
                temp = random.randint(0,1)
                if temp == 0:
                    gdzie = KIERUNEK.LEWO
                elif temp == 1:
                    gdzie = KIERUNEK.DOL


            #prawy dolny rog
            elif obecna_pozycja.y == self._swiat.getY() - 1 :
                temp = random.randint(0,1)
                if temp == 0:
                    gdzie = KIERUNEK.LEWO
                elif temp == 1:
                    gdzie = KIERUNEK.GORA


            #tylko w prawo nie moze
            else:
                temp = random.randint(0,2)
                if temp == 0:
                    gdzie = KIERUNEK.GORA
                elif temp == 1:
                    gdzie = KIERUNEK.LEWO
                elif temp == 2:
                    gdzie = KIERUNEK.DOL


        #calkiem u gory bez rogow
        elif obecna_pozycja.y == 0 :
            temp = random.randint(0,2)
            if temp == 0:
                gdzie = KIERUNEK.PRAWO
            elif temp == 1:
                gdzie = KIERUNEK.LEWO
            elif temp == 2:
                gdzie = KIERUNEK.DOL

        #calkiem na dole bez rogow
        elif obecna_pozycja.y == self._swiat.getY() - 1  :
            temp = random.randint(0,2)
            if temp == 0:
                gdzie = KIERUNEK.PRAWO
            elif temp == 1:
                gdzie = KIERUNEK.LEWO
            elif temp == 2:
                gdzie = KIERUNEK.GORA

        else:
            temp = random.randint(0,3)
            if temp == 0:
                gdzie = KIERUNEK.GORA
            elif temp == 1:
                gdzie = KIERUNEK.LEWO
            elif temp == 2:
                gdzie = KIERUNEK.DOL
            elif temp == 3:
                gdzie = KIERUNEK.PRAWO

        return gdzie

    def kolizja(self,atakujacy):
        temp = atakujacy.rysowanie() + " zjadl " + self.rysowanie() + "\n"
        self._swiat.setKomunikat(temp)
        self.setIstnieje(False)
        self._swiat.dodajOrganizm(None, self.getWsp())

    def czyOdbilAtak(self, atakujacy):
        return False



    @abstractmethod
    def dodaj(self, wsp):
        pass

    @abstractmethod
    def rysowanie(self):
        pass