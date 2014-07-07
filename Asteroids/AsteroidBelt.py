__author__ = 'jmoran'

from Asteroids import Object, Asteroid
from random import randint


class AsteroidBelt(Object):
    def __init__(self, window, game, count):
        Object.__init__(self, window, game)
        self.asteroids = []
        for i in range(0, count):
            init_point = (randint(0, self.wWidth), randint(0, self.wHeight))
            self.asteroids.append(Asteroid(self.window, self.game, init_point, 50))

    def draw(self):
        for a in self.asteroids:
            a.draw()

    def __len__(self):
        return len(self.asteroids)

    def do_collision(self, obj):
        Object.do_collision(self, obj)
        collide = 0
        if obj.no_collide:
            return collide
        idx = obj.gObj.collidelist(filter(None, [a.gObj for a in self.asteroids]))
        if idx > -1:
            collide = 1
            a = self.asteroids[idx]
            obj.do_collision(a)
            self.asteroids.extend(a.do_collision(obj.gObj))
            self.asteroids.remove(a)

        return collide