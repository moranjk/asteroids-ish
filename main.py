__author__ = 'jmoran'

import pygame
import sys

from pygame.locals import *

from Asteroids import *

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Asteroids(ish)")
pygame.key.set_repeat(30, 30)

clock = pygame.time.Clock()


ship = Ship(screen, pygame)
bullet = None

level = 1
belt = AsteroidBelt(screen, pygame, level)

while True:
    clock.tick(60)
    screen.fill(BLACK)
    if bullet:
        if bullet.draw() is False or belt.do_collision(bullet):
            bullet = None
    belt.draw()
    ship.draw()
    if belt.do_collision(ship):
        ship.crash_time = pygame.time.get_ticks()

    if ship.crashed and (ship.crash_time + 1500 < pygame.time.get_ticks()):
        ship.reset()

    if len(belt) == 0:
        level += 1
        belt = AsteroidBelt(screen, pygame, level)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            key = pygame.key.get_pressed()
            if key[K_LEFT]:
                ship.turn_left()
            if key[K_RIGHT]:
                ship.turn_right()
            if key[K_UP]:
                ship.accelerate()
            if key[K_DOWN]:
                ship.decelerate()
            if key[K_SPACE]:
                if bullet is None:
                    bullet = ship.fire()
    pygame.display.update()
