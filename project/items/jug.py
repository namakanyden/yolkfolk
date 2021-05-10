from .item import Item

class Jug(Item):
    def __init__(self, *args, **kwargs):
        super().__init__('jug_xxl', name='Jug of Water', *args, **kwargs)
