from .item import Item

class StartingHandle(Item):
    def __init__(self, *args, **kwargs):
        super().__init__('starting.handle', name = 'Starting Handle', *args, **kwargs)
