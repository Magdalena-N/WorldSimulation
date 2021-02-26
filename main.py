import pygame
import sys
from pygame.locals import *
import swiat
from Organizmy.POLOZENIE import POLOZENIE
from Organizmy.Rosliny.barszczsosnowskiego import BarszczSosnowskiego
from Organizmy.Rosliny.guarana import Guarana
from Organizmy.Rosliny.mlecz import Mlecz
from Organizmy.Rosliny.trawa import Trawa
from Organizmy.Rosliny.wilczejagody import WilczeJagody
from Organizmy.Zwierzeta.antylopa import Antylopa
from Organizmy.Zwierzeta.cyberowca import Cyberowca
from Organizmy.Zwierzeta.czlowiek import Czlowiek
from Organizmy.Zwierzeta.lis import Lis
from Organizmy.Zwierzeta.owca import Owca
from Organizmy.Zwierzeta.wilk import Wilk
from Organizmy.Zwierzeta.zolw import Zolw

width, height = 10, 10
cell_dimensions = 40
margin = 5
background_colour = (40, 40, 40)
default_title = "Magdalena Nagel 175741"


pygame.init()
pygame.font.init()

screen = pygame.display.set_mode(((cell_dimensions + margin) * width + margin,
                                  (cell_dimensions + margin) * height + margin))
pygame.display.set_caption(default_title)
screen.fill(background_colour)

swiat = swiat.Swiat(width, height, cell_dimensions, margin)
xwsp = POLOZENIE(5,8)
swiat.dodajOrganizm(Wilk(swiat, xwsp = xwsp), xwsp)
xwsp2 = POLOZENIE(3,9)
swiat.dodajOrganizm(Owca(swiat, xwsp = xwsp2), xwsp2)
xwsp0 = POLOZENIE(9,0)
swiat.dodajOrganizm(Czlowiek(swiat, xwsp = xwsp0), xwsp0)
xwsp = POLOZENIE(5,9)
swiat.dodajOrganizm(Lis(swiat, xwsp = xwsp), xwsp)
xwsp2 = POLOZENIE(5,8)
swiat.dodajOrganizm(Wilk(swiat, xwsp = xwsp2), xwsp2)
xwsp3 = POLOZENIE(4,9)
swiat.dodajOrganizm(Wilk(swiat, xwsp = xwsp3), xwsp3)
xwsp4 = POLOZENIE(6,9)
swiat.dodajOrganizm(Wilk(swiat, xwsp = xwsp4), xwsp4)
xwsp5 = POLOZENIE(1,0)
swiat.dodajOrganizm(Zolw(swiat, xwsp = xwsp5), xwsp5)
xwsp6 = POLOZENIE(4,1)
swiat.dodajOrganizm(Wilk(swiat, xwsp = xwsp6), xwsp6)
xwsp7 = POLOZENIE(2,2)
swiat.dodajOrganizm(Owca(swiat, xwsp = xwsp7), xwsp7)
xwsp8 = POLOZENIE(4,4)
swiat.dodajOrganizm(Antylopa(swiat, xwsp = xwsp8), xwsp8)
xwsp9 = POLOZENIE(2,4)
swiat.dodajOrganizm(Wilk(swiat, xwsp = xwsp9), xwsp9)
xwsp10 = POLOZENIE(0,4)
swiat.dodajOrganizm(Trawa(swiat, xwsp = xwsp10), xwsp10)
xwsp11 = POLOZENIE(9,4)
swiat.dodajOrganizm(Mlecz(swiat, xwsp = xwsp11), xwsp11)
xwsp12 = POLOZENIE(3,3)
swiat.dodajOrganizm(Guarana(swiat, xwsp = xwsp12), xwsp12)
xwsp13 = POLOZENIE(2,8)
swiat.dodajOrganizm(WilczeJagody(swiat, xwsp = xwsp13), xwsp13)

#
# xwsp14 = POLOZENIE(5,5)
# swiat.dodajOrganizm(BarszczSosnowskiego(swiat, xwsp = xwsp14), xwsp14)
# xwsp15 = POLOZENIE(1,1)
# swiat.dodajOrganizm(Cyberowca(swiat, xwsp = xwsp15), xwsp15)

for i in range(0, swiat.getY()):
    for j in range(0, swiat.getX()):
        tile = swiat._plansza.getTile(j, i)
        if not tile.empty():
            swiat._organizmy.append(tile.get_organizm())

while True:

    for event in pygame.event.get():
        if event.type is QUIT or (event.type is KEYDOWN and event.key is K_q):
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (cell_dimensions + margin)
            row = pos[1] // (cell_dimensions + margin)
            if swiat._plansza.getTile(column,row).empty():
                dodaj = True
                swiat.setKomunikat("Wybierz organizm jaki chcesz dodac:\n0. Wilk\n1. Owca\n2. Lis\n3.Zolw\n4. Antylopa\n5.Cyberowca\nF1. Trwawa\nF2. Mlecz\nF3. Guarana\nF4. BarszczSosnowskiego\nF5. WilczeJagody\nESC. WYJSCIE")
                swiat.piszKomunikat()
                while dodaj:
                    for eventt in pygame.event.get():
                        if eventt.type == K_ESCAPE:
                            dodaj = False
                            break
                        elif eventt.type == KEYDOWN and eventt.key == K_0:
                            swiat.dodajOrganizm(Wilk(swiat, xwsp = POLOZENIE(column,row)), POLOZENIE(column,row))
                            dodaj = False
                        elif eventt.type == KEYDOWN and eventt.key == K_1:
                            swiat.dodajOrganizm(Owca(swiat, xwsp = POLOZENIE(column,row)), POLOZENIE(column,row))
                            dodaj = False
                        elif eventt.type == KEYDOWN and eventt.key == K_2:
                            swiat.dodajOrganizm(Lis(swiat, xwsp = POLOZENIE(column,row)), POLOZENIE(column,row))
                            dodaj = False
                        elif eventt.type == KEYDOWN and eventt.key == K_3:
                            swiat.dodajOrganizm(Zolw(swiat, xwsp = POLOZENIE(column,row)), POLOZENIE(column,row))
                            dodaj = False
                        elif eventt.type == KEYDOWN and eventt.key == K_4:
                            swiat.dodajOrganizm(Antylopa(swiat, xwsp = POLOZENIE(column,row)), POLOZENIE(column,row))
                            dodaj = False
                        elif eventt.type == KEYDOWN and eventt.key == K_5:
                            swiat.dodajOrganizm(Cyberowca(swiat, xwsp = POLOZENIE(column,row)), POLOZENIE(column,row))
                            dodaj = False
                        elif eventt.type == KEYDOWN and eventt.key == K_F1:
                            swiat.dodajOrganizm(Trawa(swiat, xwsp = POLOZENIE(column,row)), POLOZENIE(column,row))
                            dodaj = False
                        elif eventt.type == KEYDOWN and eventt.key == K_F2:
                            swiat.dodajOrganizm(Mlecz(swiat, xwsp = POLOZENIE(column,row)), POLOZENIE(column,row))
                            dodaj = False
                        elif eventt.type == KEYDOWN and eventt.key == K_F3:
                            swiat.dodajOrganizm(Guarana(swiat, xwsp = POLOZENIE(column,row)), POLOZENIE(column,row))
                            dodaj = False
                        elif eventt.type == KEYDOWN and eventt.key == K_F4:
                            swiat.dodajOrganizm(BarszczSosnowskiego(swiat, xwsp = POLOZENIE(column,row)), POLOZENIE(column,row))
                            dodaj = False
                        elif eventt.type == KEYDOWN and eventt.key == K_F5:
                            swiat.dodajOrganizm(WilczeJagody(swiat, xwsp = POLOZENIE(column,row)), POLOZENIE(column,row))
                            dodaj = False



                for i in range(0, swiat.getY()):
                    for j in range(0, swiat.getX()):
                        tile = swiat._plansza.getTile(j, i)
                        if not tile.empty():
                            swiat._organizmy.append(tile.get_organizm())
                screen.fill(background_colour)
                swiat.render_swiat(screen, cell_dimensions, margin)
                pygame.display.update()
                pygame.time.delay(16)

        swiat.handle_event(event)
    screen.fill(background_colour)
    swiat.render_swiat(screen, cell_dimensions, margin)
    pygame.display.update()
    pygame.time.delay(16)
