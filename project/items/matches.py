from .item import Item

class Matches(Item):
    def __init__(self, *args, **kwargs):
        super().__init__('matches_xxl', name='Book of Matches', *args, **kwargs)
