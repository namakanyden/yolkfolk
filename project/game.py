# from zeromap import ZeroMap
import pytmx
from time import sleep


HEIGHT = 600
WIDTH = 800


class Context:
    def __init__(self):
        self.lifes = 3
        self.score = 0
        self.room = "the entrance"
        self.map = None


class View:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


view = View(70, 42, 23, 13)
context = Context()


def draw():
    # print('>> draw')
    global view
    screen.blit("screen", (0, 0))
    # print(viewport[1])
    # row = 10

    # for row in range(view, viewport[1] + HEIGHT//tmx.tileheight):
    #    for col in range(viewport[0], viewport[0] + WIDTH//tmx.tilewidth):

    y = 0
    for row in range(view.y, view.y + view.height):
        x = 0
        for col in range(view.x, view.x + view.width):
            image = context.map.get_tile_image(col, row, 0)
            screen.blit(
                image,
                (32 + x * context.map.tilewidth, 160 + y * context.map.tileheight),
            )
            x += 1
        y += 1

    # print score
    screen.draw.text(
        f'{context.score:02}',
        (320, 30),
        fontname="dizzy-iii-fantasy-world-dizzy-spectrum.ttf",
        fontsize=16,
        color='yellow'
    )

    # print lifes
    screen.draw.text(
        '\u25cf'*context.lifes,
        (411, 30),
        fontname="dizzy-iii-fantasy-world-dizzy-spectrum.ttf",
        fontsize=16,
        color='yellow'
    )

    # print name of the room
    screen.draw.text(
        context.room.center(33),
        (100, 79),
        fontname="dizzy-iii-fantasy-world-dizzy-spectrum.ttf",
        fontsize=16,
    )


def update():
    # print('>> update')
    global view
    # view.x += 1


def main():
    # print('>> main')
    global tmx
    context.map = pytmx.load_pygame("maps/magicland.tmx")


main()
