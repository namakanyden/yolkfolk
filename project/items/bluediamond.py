from .item import Item

class BlueDiamond(Item):
    def __init__(self, *args, **kwargs):
        super().__init__('bluediamond', name = 'Blue Diamond', *args, **kwargs)
