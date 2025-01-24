import pygame as pg
import controls
import classes

pg.init()
screen = pg.display.set_mode((800, 800))
clock = pg.time.Clock()
running = True
cs = controls.Controls()
player = classes.Player
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    keys = pg.key.get_pressed()
    if keys[cs.up.MAIN or cs.up.SECONDARY]:
        player.direction.up()
    if keys[cs.down.MAIN or cs.down.SECONDARY]:
        player.direction.down()
    if keys[cs.left.MAIN or cs.left.SECONDARY]:
        player.direction.left()
    if keys[cs.right.MAIN or cs.right.SECONDARY]:
        player.direction.right()
    screen.fill("purple")

    # RENDER

    pg.display.flip() # flips working area to display area

    dt = clock.tick(60) / 1000

pg.quit()
