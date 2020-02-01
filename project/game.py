#from zeromap import ZeroMap
import pytmx
from time import sleep


HEIGHT = 600
WIDTH = 800

class View():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

tmx = None
view = View(70, 42, 23, 13)



def draw():
    print('>> draw')
    global tmx, view
    screen.blit('screen', (0, 0))
    #print(viewport[1])
    #row = 10

    #for row in range(view, viewport[1] + HEIGHT//tmx.tileheight):
    #    for col in range(viewport[0], viewport[0] + WIDTH//tmx.tilewidth):

    y = 0
    for row in range(view.y, view.y + view.height):
        x = 0
        for col in range(view.x, view.x + view.width):
            image = tmx.get_tile_image(col, row, 0)
            screen.blit(image, (32 + x*tmx.tilewidth, 160+y*tmx.tileheight))
            x+= 1
        y+=1


def update():
    print('>> update')
    global view
    view.x += 1


def main():
    print('>> main')
    global tmx
    tmx = pytmx.load_pygame('maps/magicland.tmx')



main()
