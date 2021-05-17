from pgzero.actor import Actor
from pgzero import game
from time import time

WIDTH = 800


class AnimatedActor(Actor):
    def __init__(self, *args, pingpong=False, duration=100, **kwargs):
        super().__init__(*args, **kwargs)
        self.pingpong = pingpong
        self.duration = duration
        self._stopped = False
        self._frames = []
        # TODO make it required: sprite
        self.set_image(self.image, dimension=kwargs['sprite'])

    def start(self):
        self._stopped = False

    def stop(self):
        self._stopped = True

    def set_image(self, image, dimension):
        px, py = self.pos
        tx, ty = self.topleft
        self.image = image
        self.height = dimension[1]
        self.width = dimension[0]
        self._frames = []

        # self._init_position(pos=None, anchor=self.anchor, sprite=dimension)

        # counting that sprites will be same size
        self.pos = (px, py)
        self.topleft = (tx, ty)

        for x_offset in range(int(self._orig_surf.get_width() / self.width)):
            surface = self._orig_surf.subsurface(
                (x_offset * self.width, 0, self.width, self.height))
            self._frames.append(surface)

        # frame config
        self._current_frame = 0
        self.frame_duration = self.duration / len(self._frames)
        self.last_frame_update = time() * 1000
        self._next_frame_dx = 1
        # return self._current_frame

    @property
    def current_frame(self):
        return self._current_frame

    @current_frame.setter
    def current_frame(self, index):
        if 0 < index < len(self._frames) - 1:
            raise 'Frame index out of range.'
        self._current_frame = index

    def _update_frame(self):
        # if not self._stopped:
        if True:
            now = time() * 1000
            if now - self.last_frame_update > self.frame_duration:
                self.last_frame_update = now
                self._current_frame += self._next_frame_dx

                if self.pingpong:
                    if self._next_frame_dx == 1 and self._current_frame >= len(self._frames) - 1 or self._next_frame_dx == -1 and self._current_frame <= 0:
                        self._next_frame_dx *= -1
                else:
                    if self._current_frame == len(self._frames):
                        self._current_frame = 0


    def draw(self):
        self._update_frame()
        print(self._current_frame)
        game.screen.blit(self._frames[self._current_frame], self.topleft)

