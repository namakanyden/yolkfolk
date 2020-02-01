from .item import Item

class Sword(Item):
    def __init__(self, pos):
        super().__init__('sword', name='Sword')
        self.pos = pos
