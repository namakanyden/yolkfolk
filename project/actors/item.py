from pgzero.actor import Actor

class Item(Actor):
    def __init__(self, *args, name, **kwargs):
        super().__init__(*args, **kwargs)
        self._name = name

    def get_name(self):
        return self._name

    def __str__(self):
        return self._name
