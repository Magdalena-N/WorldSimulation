import random
from Organizmy.KIERUNEK import KIERUNEK
from Organizmy.POLOZENIE import POLOZENIE
from Organizmy.organizm import Organizm
from abc import ABC, abstractmethod


class Zwierze (Organizm):

    def __init__(self, xswiat, xsila, xinicjatywa, xwsp, xwiek):
        super().__init__(xswiat, xsila, xinicjatywa, xwsp, xwiek)

    def akcja(self):
        czyRuchMozliwy = True
        wsp2 = POLOZENIE(self.getWsp().x, self.getWsp().y)

        if self.getNastepnyKierunek() == KIERUNEK.BRAK and self.rysowanie() != "?":
            gdzie = self.losujKierunek(self, self.getZasieg())
        else:
            gdzie = self.getNastepnyKierunek()
            if gdzie == KIERUNEK.GORA and wsp2.y - 1 < 0 or \
                gdzie == KIERUNEK.DOL and wsp2.y + 1 > self._swiat.getY() - 1 or \
                gdzie == KIERUNEK.LEWO and wsp2.x - 1 < 0 or \
                gdzie == KIERUNEK.PRAWO and wsp2.x + 1 > self._swiat.getX() - 1 or \
                gdzie == KIERUNEK.BRAK:
                    czyRuchMozliwy = False

        if czyRuchMozliwy:

            if self.czyWolne(gdzie, self.getZasieg()):
                self.ruch(self, gdzie)
            else:
                if gdzie == KIERUNEK.GORA:
                    wsp2.y -= self.getZasieg()
                elif gdzie == KIERUNEK.DOL:
                    wsp2.y += self.getZasieg()
                elif gdzie == KIERUNEK.LEWO:
                    wsp2.x -= self.getZasieg()
                elif gdzie == KIERUNEK.PRAWO:
                    wsp2.x += self.getZasieg()

                if 0 <= wsp2.x < self._swiat.getX() and  0 <= wsp2.y < self._swiat.getY():
                    self._swiat.getOrganizm(wsp2).kolizja(self)

                if 0 <= wsp2.x < self._swiat.getX() and  0 <= wsp2.y < self._swiat.getY() and \
                        self._swiat.getOrganizm(self.getWsp()) is not None and self.getOdbity() is False and \
                        self.getRozmnozone() is False:
                    self.ruch(self, gdzie)
                elif self._swiat.getOrganizm(self.getWsp()) is not None:
                    self.setOdbity(False)
                    self.setRozmnozone(False)

    def czyWolne(self,gdzie, zasieg):
        pozycja = POLOZENIE(self.getWsp().x, self.getWsp().y)

        if gdzie == KIERUNEK.GORA:
            pozycja.y -= zasieg
        elif gdzie == KIERUNEK.DOL:
            pozycja.y += zasieg
        elif gdzie == KIERUNEK.LEWO:
            pozycja.x -= zasieg
        elif gdzie == KIERUNEK.PRAWO:
            pozycja.x += zasieg

        if 0 <= pozycja.x < self._swiat.getX() and \
                0 <= pozycja.y < self._swiat.getY() and \
                self._swiat._plansza.getTile(pozycja.x,pozycja.y).empty():
            return True
        # if self._swiat.getOrganizm(pozycja) is None:
        #     return True

        else:
            return False

    def losujKierunek(self, org, zasieg):

        gdzie = KIERUNEK.BRAK
        obecna_pozycja = org.getWsp()

        #obiekt calkiem z lewej
        if obecna_pozycja.x == 0 or obecna_pozycja.x == zasieg - 1:
            #lewy gorny rog(PRAWO,DOL)
            if obecna_pozycja.y == 0 or obecna_pozycja.y == zasieg - 1:
                temp = random.randint(0,1)
                if temp == 0:
                    gdzie = KIERUNEK.PRAWO
                elif temp == 1:
                    gdzie = KIERUNEK.DOL

            #lewy dolny rog (GORA,PRAWO)
            elif obecna_pozycja.y == self._swiat.getY() - 1 or obecna_pozycja.y == self._swiat.getY() - zasieg:
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
        elif obecna_pozycja.x == self._swiat.getX() - 1 or obecna_pozycja.x == self._swiat.getX() - zasieg:
            #prawy gorny rog
            if obecna_pozycja.y == 0 or obecna_pozycja.y == zasieg - 1:
                temp = random.randint(0,1)
                if temp == 0:
                    gdzie = KIERUNEK.LEWO
                elif temp == 1:
                    gdzie = KIERUNEK.DOL


            #prawy dolny rog
            elif obecna_pozycja.y == self._swiat.getY() - 1 or obecna_pozycja.y == self._swiat.getY() - zasieg :
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
        elif obecna_pozycja.y == 0 or obecna_pozycja.y == zasieg - 1:
            temp = random.randint(0,2)
            if temp == 0:
                gdzie = KIERUNEK.PRAWO
            elif temp == 1:
                gdzie = KIERUNEK.LEWO
            elif temp == 2:
                gdzie = KIERUNEK.DOL

        #calkiem na dole bez rogow
        elif obecna_pozycja.y == self._swiat.getY() - 1 or obecna_pozycja.y == self._swiat.getY() - zasieg :
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

    def czyOdbilAtak(self, atakujacy):
        return False

    def rozmnoz(self, gdzie):
        wsp2 = POLOZENIE(self.getWsp().x, self.getWsp().y)
        if gdzie == KIERUNEK.GORA:
            wsp2.y -= 1
        elif gdzie == KIERUNEK.DOL:
            wsp2.y += 1
        elif gdzie == KIERUNEK.LEWO:
            wsp2.x -= 1
        elif gdzie == KIERUNEK.PRAWO:
            wsp2.x += 1

        if self.czyWolne(gdzie, 1):

            self.dodaj(wsp2)

    @abstractmethod
    def dodaj(self, wsp):
        pass

    def kolizja(self, atakujacy):

        if self.rysowanie() == atakujacy.rysowanie():
            gdzie = self.losujKierunek(self,1)
            self.rozmnoz(gdzie)

            atakujacy.setRozmnozone(True)
            temp = ""
            temp = self.rysowanie() + " rozmnozyly sie. \n"
            self._swiat.setKomunikat(temp)
            # pass

        else:
            #sila zaatakowanego mniejsza/rowna od atakujacego ginie zaatakowany
            if self.getSila() <= atakujacy.getSila():
                temp = ""
                temp = atakujacy.rysowanie() + " zabil/a " + self.rysowanie() + "\n"
                self._swiat.setKomunikat(temp)
                self.setIstnieje(False)

                self._swiat.dodajOrganizm(None, self.getWsp())

                #w przeciwnym wypadku sila zaatakowanego wieksza ginie atakujacy
            else:
                temp = ""
                temp += self.rysowanie() + " zabil/a " + atakujacy.rysowanie() + "\n"

                self._swiat.setKomunikat(temp)
                atakujacy.setIstnieje(False)

                self._swiat.dodajOrganizm(None, atakujacy.getWsp())

    def ruch(self, org, gdzie):
        wsp1 = org.getWsp()
        wsp2 = POLOZENIE(org.getWsp().x, org.getWsp().y)

        if gdzie == KIERUNEK.GORA:
            wsp2.y -= org.getZasieg()
        elif gdzie == KIERUNEK.DOL:
            wsp2.y += org.getZasieg()
        elif gdzie == KIERUNEK.LEWO:
            wsp2.x -= org.getZasieg()
        elif gdzie == KIERUNEK.PRAWO:
            wsp2.x += org.getZasieg()

        org.setWsp(wsp2)
        self._swiat.dodajOrganizm(org, wsp2)
        self._swiat.dodajOrganizm(None, wsp1)
