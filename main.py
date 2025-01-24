import pygame as pg

pg.init()
screen = pg.display.set_mode((800, 800))
clock = pg.time.Clock()
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill("purple")

    # RENDER

    pg.display.flip() # flips working area to display area

    clock.tick(60)

pg.quit()

