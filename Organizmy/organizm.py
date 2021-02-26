from abc import ABC, abstractmethod
import pygame
from pygame.rect import Rect
from Organizmy.KIERUNEK import KIERUNEK


class Organizm(ABC):

    def __init__(self, xswiat,  xsila, xinicjatywa, xwsp, xwiek):
        self._swiat=xswiat
        self.__nastepny_kierunek = KIERUNEK.BRAK
        self.__sila = xsila
        self.__inicjatywa = xinicjatywa
        self.__wsp = xwsp
        self.__wiek = xwiek
        self.__istnieje = True
        self.__odbity = False
        self.__zasieg = 1
        self.__rozmnozone = False
        self.__umiejetnosc = False
        self.__kolor = (255,255,255)

    def getSila(self):
        return self.__sila

    def setSila(self, xsila):
        self.__sila = xsila

    def getInicjatywa(self):
        return self.__inicjatywa

    def setInicjatywa(self, xinicjatywa):
        self.__inicjatywa = xinicjatywa

    def getWiek(self):
        return self.__wiek

    def setWiek(self, xwiek):
        self.__wiek = xwiek

    def getWsp(self):
        return self.__wsp

    def setWsp(self, xwsp):
        self.__wsp = xwsp

    def getNastepnyKierunek(self):
        return self.__nastepny_kierunek

    def setNastepnyKierunek(self, n_k):
        self.__nastepny_kierunek = n_k

    def getIstnieje(self):
        return self.__istnieje

    def setIstnieje(self, xistnieje):
        self.__istnieje = xistnieje

    def getOdbity(self):
        return self.__odbity

    def setOdbity(self, xodbity):
        self.__odbity = xodbity

    def getZasieg(self):
        return self.__zasieg

    def setZasieg(self, xzasieg):
        self.__zasieg = xzasieg

    def getRozmnozone(self):
        return self.__rozmnozone

    def setRozmnozone(self, czyRozmnozone):
        self.__rozmnozone = czyRozmnozone

    def setUmiejetnosc(self, aktywowac):
        self.__umiejetnosc = aktywowac


    def getUmiejetnosc(self):
        return self.__umiejetnosc

    def setKolor(self, xkolor):
        self.__kolor=xkolor

    def getKolor(self):
        return self.__kolor

    @abstractmethod
    def rysowanie(self):
        pass

    @abstractmethod
    def akcja(self):
        pass

    @abstractmethod
    def kolizja(self, atakujacy):
        pass

    @abstractmethod
    def czyOdbilAtak(self, atakujacy):
        pass

    # def render(self, screen, cell_dimensions, margin):
    #     if self.getIstnieje():
    #         pygame.draw.rect(screen, self._kolor, Rect(margin + self.getWsp().x * (cell_dimensions + margin),
    #                     margin + self.getWsp().y * (cell_dimensions + margin),
    #                     cell_dimensions,cell_dimensions))
