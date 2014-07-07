__author__ = 'jmoran'


class Object:
    gObj = None
    point = None

    def __init__(self, window, game):
        self.window = window
        self.wHeight = window.get_height()
        self.wWidth = window.get_width()
        self.game = game
        self.no_collide = False

    def do_collision(self, obj):
        return
