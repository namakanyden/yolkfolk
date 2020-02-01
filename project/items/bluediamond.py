from .item import Item

class BlueDiamond(Item):
    def __init__(self, pos):
        super().__init__('bluediamond', name = 'Blue Diamond')
        self.pos = pos
