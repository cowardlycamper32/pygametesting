import math


class entity:
    def __init__(self):
        self.health = 0
        self.speed = 0
        self.position = self.position()
        self.direction = self.direction()

    def move(self, dt):
        self.direction.vectorNormalisation()
        self.direction.cap()
        self.position.x += self.direction.x * self.speed * dt
        self.position.y += self.direction.y * self.speed * dt



    class position:
        def __init__(self, x = 0, y = 0):
            self.x = x
            self.y = y

    class direction:
        def __init__(self):
            self.x = 0
            self.y = 0

        def vectorNormalisation(self):
            length = math.sqrt(self.x^2 + self.y^2)
            if length > 0:
                self.x /= length
                self.y /= length

        def cap(self):
            if self.x > 1:
                self.x = 1
            if self.x < -1:
                self.x = -1
            if self.y > 1:
                self.y = 1
            if self.y < -1:
                self.y = -1

        def up(self):
            self.y += 1
        def down(self):
            self.y -= 1
        def left(self):
            self.x -= 1
        def right(self):
            self.x += 1



class Player(entity):
    def __init__(self):
        entity.__init__(self)
        self.health = 100
        self.speed = 2
        self.position = entity.position(50, 50)