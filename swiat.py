from pygame.locals import *
import pygame

from Organizmy.POLOZENIE import POLOZENIE
from Organizmy.Zwierzeta.wilk import Wilk
from plansza import Plansza
from Organizmy.KIERUNEK import KIERUNEK
import pickle
import csv

class Swiat:
    __empty_tile_colour = (70, 70, 70)

    def __init__(self, x, y, cell_dimensions, margin):
        self.__x = x
        self.__y = y
        self._plansza = Plansza(x, y)
        self.__czlowiekZyje =False
        self.__komunikat = ""
        self._organizmy = []
        # self.screen = screen
        self.cell_dimensions = cell_dimensions
        self.margin = margin
        self.runda = 0

    def setCzlowiekZyje(self,zyje):
        self.__czlowiekZyje = zyje

    def getCzlowiekZyje(self):
        return self.__czlowiekZyje

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def wykonajTure(self):

        self.runda += 1
        self.__komunikat += "Runda: " + str(self.runda) + "\n"
        self._organizmy.clear()

        for i in range(0,self.__y):
            for j in range(0,self.__x):
                tile = self._plansza.getTile(j, i)
                if not tile.empty():
                    self._organizmy.append(tile.get_organizm())

        for org in self._organizmy:
            org.setWiek(org.getWiek()+1)

        self._organizmy.sort(key=lambda organizm: organizm.getWiek(), reverse=True)

        self._organizmy.sort(key=lambda organizm: organizm.getInicjatywa(), reverse=True)

        for it in self._organizmy:
            if it.getIstnieje():
                it.akcja()

        self.piszKomunikat()

    def getOrganizm(self, pozycja):
        return self._plansza.getTile(pozycja.x, pozycja.y).get_organizm()

    def dodajOrganizm(self, xorgan, pozycja):
        self._plansza.getTile(pozycja.x, pozycja.y).set_organizm(xorgan)
        self._plansza.getTile(pozycja.x, pozycja.y).set_pozycja(pozycja)

    def setKomunikat(self,xlog):
        self.__komunikat += xlog

    def getKomunikat(self):
        return self.__komunikat

    def piszKomunikat(self):
        if not self.__komunikat == "":
            print(self.__komunikat)
            self.__komunikat = ""

    def uruchomUmiejetnosc(self):

        for i in range(0,self.__y):
            for j in range(0,self.__x):
                if not self._plansza.getTile(j,i).empty()  and \
                        self._plansza.getTile(j,i).get_organizm().rysowanie() == "?":
                    self._plansza.getTile(j,i).get_organizm().setUmiejetnosc(True)

    def ustawKierunekCzlowiekowi(self,kierunek):
        for i in range(0,self.__y):
            for j in range(0, self.__x):
                if not self._plansza.getTile(j, i).empty()  and \
                        self._plansza.getTile(j, i).get_organizm().rysowanie() == "?":
                    self._plansza.getTile(j, i).get_organizm().setNastepnyKierunek(kierunek)

    def render_swiat(self, screen, cell_dimensions, margin):
        self._cell_dimension = cell_dimensions
        self._cell_margin = margin
        self._rysuj_grid(screen, cell_dimensions, margin)
        for organizm in self._organizmy:
            if organizm.getIstnieje():
                self.render(screen, cell_dimensions, margin,organizm.getKolor(),organizm.getWsp())
            # organizm.render(screen, cell_dimensions, margin)


    def _rysuj_grid(self, screen, cell_dimensions, margin):

        rect = Rect(-cell_dimensions, -cell_dimensions, cell_dimensions, cell_dimensions)
        for y in range(self.getY()):
            rect.y += cell_dimensions + margin
            rect.x = -cell_dimensions
            for x in range(self.getX()):
                rect.x += cell_dimensions + margin
                pygame.draw.rect(screen, self.__empty_tile_colour, rect)

    def handle_event(self, event):
        if event.type is KEYDOWN:
            # next turn
            if event.key is K_n:
                self.wykonajTure()
            # player movement
            elif event.key is K_w:
                self.ustawKierunekCzlowiekowi(KIERUNEK.GORA)
            elif event.key is K_d:
                self.ustawKierunekCzlowiekowi(KIERUNEK.PRAWO)
            elif event.key is K_s:
                self.ustawKierunekCzlowiekowi(KIERUNEK.DOL)
            elif event.key is K_a:
                self.ustawKierunekCzlowiekowi(KIERUNEK.LEWO)
            elif event.key == K_u:
                self.uruchomUmiejetnosc()
            elif event.key == K_z:
                self.save()
            elif event.key == K_l:
                self.load()



    def render(self, screen, cell_dimensions, margin, kolor, wsp):
        pygame.draw.rect(screen, kolor, Rect(margin + wsp.x * (cell_dimensions + margin),
                                             margin + wsp.y * (cell_dimensions + margin),
                                             cell_dimensions, cell_dimensions))

    def save(self):
        print("Zapisano swiat")
        mylist = self._plansza.getPlansza()

        with open('mylist', 'wb') as f:
            pickle.dump(mylist, f)


    def load(self):
        print("Wczytano swiat")
        with open('mylist', 'rb') as f:
             obiekt = pickle.load(f)
        self._plansza.setPlansza(obiekt)


