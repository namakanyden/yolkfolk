from pgzero.builtins import Actor


class Item(Actor):
    def __init__(self, *args, name, **kwargs):
        super().__init__(*args, **kwargs)
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def tile_pos(self):
        return (self.x // 16, self.y // 16)

    @property
    def tile_x(self):
        return self.x // 16

    @property
    def tile_y(self):
        return self.y // 16

    def __str__(self):
        return self._name

    # TODO mozno treba iny typ na update()
    def update(self):
        pass
