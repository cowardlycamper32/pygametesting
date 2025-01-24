import pygame as pg

class Controls:
    def __init__(self):
        self.up = self.up()
        self.down = self.down()
        self.left = self.left()
        self.right = self.right()
        self.exit = self.exit()

    class up:
        def __init__(self):
            self.MAIN = pg.K_w
            self.SECONDARY = pg.K_UP

    class down:
        def __init__(self):
            self.MAIN = pg.K_s
            self.SECONDARY = pg.K_DOWN

    class left:
        def __init__(self):
            self.MAIN = pg.K_a
            self.SECONDARY = pg.K_LEFT

    class right:
        def __init__(self):
            self.MAIN = pg.K_d
            self.SECONDARY = pg.K_RIGHT

    class exit:
        def __init__(self):
            self.MAIN = pg.K_ESCAPE
            self.SECONDARY = pg.K_ESCAPE
