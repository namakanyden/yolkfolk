# from zeromap import ZeroMap
import pytmx
from time import sleep
from items import BlueDiamond, Sword


HEIGHT = 600
WIDTH = 800


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


class View:
    def __init__(self, context, x, y, width, height):
        self.context = context
        self.x = x  # tile x
        self.y = y  # tile y
        self.width = width  # width in tiles
        self.height = height  # width in tiles

    # TODO zamysliet sa nad nazvom: view.contains_actor(actor)
    # TODO actor in view
    def is_actor_visible(self, actor):
        return (
            self.x * self.context.map.tilewidth
            <= actor.x
            <= (self.x + self.width) * self.context.map.tilewidth
            and self.y * self.context.map.tileheight
            <= actor.y
            <= (self.y + self.height) * self.context.map.tileheight
        )


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
view = View(context, 310, 30, 46, 22)
# view = View(0, 0, 46, 22)


def draw():
    global view
    screen.blit("screen", (0, 0))
    # print(viewport[1])
    # row = 10
    view_offset_x = 32
    view_offset_y = 160

    # draw background
    y = 0
    for row in range(view.y, view.y + view.height):
        x = 0
        for col in range(view.x, view.x + view.width):
            image = context.map.get_tile_image(col, row, 0)
            screen.blit(
                image,
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
        (320, 30),
        fontname="dizzy-iii-fantasy-world-dizzy-spectrum.ttf",
        fontsize=16,
        color="yellow",
    )

    # print lifes
    screen.draw.text(
        "\u25cf" * context.lifes,
        (411, 30),
        fontname="dizzy-iii-fantasy-world-dizzy-spectrum.ttf",
        fontsize=16,
        color="yellow",
    )

    # print name of the room
    screen.draw.text(
        context.room.center(33),
        (100, 79),
        fontname="dizzy-iii-fantasy-world-dizzy-spectrum.ttf",
        fontsize=16,
    )

    # draw actors
    for actor in context.actors:
        # check if in viewport
        if view.is_actor_visible(actor):
            old_pos = actor.pos
            print(actor, actor.pos)
            actor.x = (actor.tile_x - view.x)*16 + view_offset_x
            actor.y = (actor.tile_y - view.y)*16 + view_offset_y
            actor.draw()
            print(actor, actor.pos)
            actor.pos = old_pos


    Dialog("jano je proste namakany makac jeden velky", 15, "white").draw()
    # d.draw()


def update():
    global view
    # view.x += 1


def main():
    context.map = pytmx.load_pygame("maps/magicland.tmx")

    for actor in context.map.get_layer_by_name("actors"):
        pos = (actor.x, actor.y)

        if actor.name == "BlueDiamond":
            context.actors.append(BlueDiamond(pos))
        elif actor.name == "Sword":
            context.actors.append(Sword(pos))

        # print(actor)


main()
