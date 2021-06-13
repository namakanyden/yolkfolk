import pygame
import pytmx
from pgzero.actor import Actor
from settings import WIDTH, HEIGHT, TITLE, ICON
from context import Context
from view import View

context = Context()
view = View(context, 0, 0, 32, 24)


def can_actor_move(pos_x, pos_y):
    walls = context.map.get_layer_by_name("walls")
    pos_x = pos_x // 32
    pos_y = pos_y // 32
    for wall in walls.tiles():
        x, y, data = wall
        if pos_x == x and pos_y == y:
            return False

    return True


def draw():
    global view

    screen.clear()

    wallpaper = pygame.image.load("images/screen-orig.png").convert()
    screen.blit(wallpaper, (0,0))



    # draw background
    y = 0
    for row in range(view.top, view.top + view.height):
        x = 0
        for col in range(view.left, view.left + view.width):
            image = context.map.get_tile_image(col, row, 0)
            if image is not None:
                screen.blit(image,
                            (
                                context.view_offset_x + x * context.map.tilewidth,
                                context.view_offset_y + y * context.map.tileheight,
                            ),
                            )
            x += 1
        y += 1

    # # print score
    # screen.draw.text(
    #     f"{context.score:02}",
    #     (32 * 13, 32 * 1),
    #     fontname="dizzy-iii-fantasy-world-dizzy-spectrum.ttf",
    #     fontsize=27,
    #     color="yellow",
    # )
    #
    # # print lifes
    # screen.draw.text(
    #     "\u25cf" * context.lifes,
    #     (32 * 16, 32 * 1),
    #     fontname="dizzy-iii-fantasy-world-dizzy-spectrum.ttf",
    #     fontsize=27,
    #     color="yellow",
    # )
    #
    # # print name of the room
    # screen.draw.text(
    #     context.room.center(25),
    #     (32 * 4, 32 * 3),
    #     fontname="dizzy-iii-fantasy-world-dizzy-spectrum.ttf",
    #     fontsize=27,
    # )
    for actor in context.actors:
        actor.draw()



def update():
    actor = context.actors[0]

    if keyboard.left:
        # view.move_view(ViewMovement.LEFT)
        new_pos = actor.x - 3
        if can_actor_move(new_pos, actor.y):
            actor.x -= 3

    if keyboard.right:
        # view.move_view(ViewMovement.RIGHT)
        new_pos = actor.x + 3
        if can_actor_move(new_pos, actor.y):
            actor.x += 3

    if keyboard.up:
        # view.move_view(ViewMovement.UP)
        new_pos = actor.y - 3
        if can_actor_move(actor.x, new_pos):
            actor.y -= 3

    if keyboard.down:
        # view.move_view(ViewMovement.DOWN)
        new_pos = actor.y + 3
        if can_actor_move(actor.x, new_pos):
            actor.y += 3


def main():
    context.map = pytmx.load_pygame("../maps/dizzy-main-map.tmx")

    for actor in context.map.get_layer_by_name("actors"):
        temp_actor = None

        if actor.name == "jug":
            temp_actor = Actor("32x/jug")
        if actor.name == "leaves":
            temp_actor = Actor("32x/leaves")

        if actor.name == "door":
            temp_actor = Actor("32x/door")

        if temp_actor:
            temp_actor.left, temp_actor.top = context.view_offset_x + actor.x, context.view_offset_y + actor.y
            context.actors.append(temp_actor)
            print(context.actors)

# main()

if __name__ == '__main__':
    import pgzrun

    main()
    pgzrun.go()
