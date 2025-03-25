import pygame
import math


pygame.init()


win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Przekształcenia")

NIEBIESKI = (0, 255, 0)


oryginalne_punkty = [(300, 100), (400, 200), (350, 350), (250, 350), (200, 200)]
punkty = oryginalne_punkty[:]



def obroc_punkty(kat):
    kat = math.radians(kat)
    return [(300 + (x - 300) * math.cos(kat) - (y - 300) * math.sin(kat),
             300 + (x - 300) * math.sin(kat) + (y - 300) * math.cos(kat))
            for x, y in oryginalne_punkty]



def przeksztalc_pieciokat(numer):
    global punkty
    if numer == 1:
        punkty = [(x * 0.5 + 150, y * 0.5 + 150) for x, y in oryginalne_punkty]
    elif numer == 2:
        punkty = obroc_punkty(45)
    elif numer == 3:
        punkty = obroc_punkty(90)
    elif numer == 4:
        punkty = [(x + (y - 300) * 0.5, y) for x, y in oryginalne_punkty]
    elif numer == 5:
        punkty = [(x, y * 0.7 + 90) for x, y in oryginalne_punkty]
    elif numer == 6:
        temp = obroc_punkty(90)
        punkty = [(x + (y - 300) * 0.5, y) for x, y in temp]
    elif numer == 7:
        temp = obroc_punkty(90)
        punkty = [(x, y * 0.7 + 90) for x, y in temp]
    elif numer == 8:
        temp = obroc_punkty(45)
        punkty = [(x, y * 0.7 + 90) for x, y in temp]
    elif numer == 9:
        temp = obroc_punkty(90)
        temp = [(x + (y - 300) * 0.5, y) for x, y in temp]
        punkty = [(x + (y - 300) * 0.5, y) for x, y in temp]
    else:
        punkty = oryginalne_punkty[:]



run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if pygame.K_1 <= event.key <= pygame.K_9:
                przeksztalc_pieciokat(event.key - pygame.K_0)


    win.fill((0, 0, 0))


    pygame.draw.polygon(win, NIEBIESKI, punkty)


    pygame.display.update()


pygame.quit()