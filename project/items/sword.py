from .item import Item

class Sword(Item):
    def __init__(self, *args, **kwargs):
        super().__init__('sword', name='Sword', *args, **kwargs)
