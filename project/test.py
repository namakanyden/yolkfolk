#!/usr/bin/env pgzrun

# from zeromap import ZeroMap
import pygame
import pytmx
from time import sleep
# from .items import StartingHandle
from settings import WIDTH, HEIGHT, TITLE, ICON


class Context:
    def __init__(self):
        self.lifes = 3
        self.score = 0
        self.room = "the entrance"
        self.map = None
        self.actors = []


class World:
    def __init__(self):
        self.actors = []


class ViewMovement:
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4


class View:
    def __init__(self, context, left, top, width, height):
        self.context = context
        self.left = left  # tile x
        self.top = top  # tile y
        self.width = width  # width in tiles
        self.height = height  # width in tiles

    # TODO zamysliet sa nad nazvom: view.contains_actor(actor)
    # TODO actor in view
    def is_actor_visible(self, actor):
        return (
                self.left * self.context.map.tilewidth
                <= actor.left
                <= (self.left + self.width) * self.context.map.tilewidth
                and self.top * self.context.map.tileheight
                <= actor.top
                <= (self.top + self.height) * self.context.map.tileheight
        )

    def move_view(self, view_movement: int):
        if view_movement == ViewMovement.RIGHT:
            if self.left + self.width < self.context.map.width:
                self.left += 1
        elif view_movement == ViewMovement.LEFT:
            if self.left > 0:
                self.left -= 1
        elif view_movement == ViewMovement.UP:
            if self.top > 0:
                self.top -= 1
        else:
            if self.top + self.height < self.context.map.height:
                self.top += 1


class Dialog(object):
    def __init__(self, text, width, color="white"):
        self._width = width
        self._color = color

        self._lines = []
        line = ""
        for word in text.split():
            if len(line) + len(word) < self._width:
                line = f"{line} {word}"
            else:
                self._lines.append(line.center(self._width))
                line = word

    def draw(self):
        # count the position first
        y_offset = HEIGHT / 2 - 16 * len(self._lines) / 2
        x_offset = WIDTH / 2 - 16 * self._width / 2

        # print line by line
        counter = 0
        for line in self._lines:
            screen.draw.text(
                line,
                (x_offset, counter * 20 + y_offset),
                fontname="dizzy-iii-fantasy-world-dizzy-spectrum.ttf",
                fontsize=16,
                color=self._color,
            )
            counter += 1


context = Context()
view = View(context, 0, 0, 32, 24)


def draw():
    global view

    screen.clear()

    # wallpaper = pygame.image.load("maps/dizzy.3.5.background.32x32.png").convert()
    # screen.blit(wallpaper, (-view.left * 32, -view.top * 32))


    view_offset_x = 0
    view_offset_y = 0

    # draw background
    y = 0
    for row in range(view.top, view.top + view.height):
        x = 0
        for col in range(view.left, view.left + view.width):
            image = context.map.get_tile_image(col, row, 0)
            if image is not None:
                screen.blit(image,
                            (
                                view_offset_x + x * context.map.tilewidth,
                                view_offset_y + y * context.map.tileheight,
                            ),
                            )
            x += 1
        y += 1

    # print score
    screen.draw.text(
        f"{context.score:02}",
        (32 * 13, 32 * 1),
        fontname="dizzy-iii-fantasy-world-dizzy-spectrum.ttf",
        fontsize=27,
        color="yellow",
    )

    # print lifes
    screen.draw.text(
        "\u25cf" * context.lifes,
        (32 * 16, 32 * 1),
        fontname="dizzy-iii-fantasy-world-dizzy-spectrum.ttf",
        fontsize=27,
        color="yellow",
    )

    # print name of the room
    screen.draw.text(
        context.room.center(25),
        (32 * 4, 32 * 3),
        fontname="dizzy-iii-fantasy-world-dizzy-spectrum.ttf",
        fontsize=27,
    )
    # draw actors
    # for actor in context.actors:
    #    # check if in viewport
    #    if view.is_actor_visible(actor):
    #        old_pos = actor.pos
    #        print(actor, actor.pos)
    #        actor.x = (actor.tile_x - view.x)*16 + view_offset_x
    #        actor.y = (actor.tile_y - view.y)*16 + view_offset_y
    #        actor.draw()
    #        print(actor, actor.pos)
    #        actor.pos = old_pos

    # Dialog("jano je proste namakany makac jeden velky", 15, "white").draw()
    # d.draw()


def update():
    # if keyboard.left:
    #     view.move_view(ViewMovement.LEFT)
    #
    # if keyboard.right:
    #     view.move_view(ViewMovement.RIGHT)
    #
    # if keyboard.up:
    #     view.move_view(ViewMovement.UP)
    #
    # if keyboard.down:
    #     view.move_view(ViewMovement.DOWN)


def main():
    context.map = pytmx.load_pygame("maps/dizzy-main-map.tmx")

    for actor in context.map.get_layer_by_name("actors"):
        pos = (actor.x, actor.y)

        if actor.name == "dizzy":
            # TODO pridat dizziho
            pass


        print(actor)


# main()

if __name__ == '__main__':
    import pgzrun

    main()
    pgzrun.go()
