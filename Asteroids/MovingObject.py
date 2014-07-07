__author__ = 'jmoran'

from Asteroids import Object


class MovingObject(Object):
    def __init__(self, window, game, init_point, slope):
        Object.__init__(self, window, game)
        self.point = init_point
        self.slope = slope
