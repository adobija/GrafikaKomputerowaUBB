import pygame

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Koło z kwadratem")

# Deklarowanie kolorów
CZARNY = (0, 0, 0)
ZOLTY = (255, 255, 0)
BIALY = (255, 255, 255)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Wypełnienie tła
    win.fill(BIALY)

    # Rysowanie czarnego koła
    center = (300, 300)
    radius = 150
    pygame.draw.circle(win, CZARNY, center, radius)

    # Rysowanie żółtego kwadratu w środku koła
    square_size = 100
    square_x = center[0] - square_size // 2
    square_y = center[1] - square_size // 2
    pygame.draw.rect(win, ZOLTY, (square_x, square_y, square_size, square_size))

    pygame.display.update()

pygame.quit()