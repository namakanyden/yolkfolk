# from animate_actor import AnimatedActor
from pgzero.constants import keys
from DizzyActor import DizzyActor


def draw():
    screen.clear()
    braid.draw()


def update(dt):
    braid.update(keyboard)
    # braid.update("left")
    # if keyboard.space:

    #     if braid._stopped:
    #         print("dizzy")
    #         braid.set_image("braid_run", dimension=(130, 150))
    #         braid.start()
    #         # keyboard.leftkeyboard.left
    #     else:
    #         print("braid")
    #         braid.stop()
    #         braid.set_image("dizzy", dimension=(25, 25))



braid = DizzyActor()

