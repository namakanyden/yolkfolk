#!/usr/bin/env pgzero

from items.matches import Matches
from items.jug import Jug
from settings import WIDTH, HEIGHT, TITLE


actors = []


def draw():
    screen.blit('trapped_xxl', (0,0))

    for actor in actors:
        print(actor)
        actor.draw()

def update():
    for actor in actors:
        actor.update()



def init():
    actors.append(Jug(pos=(88 * 6, 88 * 5)))
    actors.append(Matches(pos=(88 * 12 - 44, 88 * 5)))
 

init()