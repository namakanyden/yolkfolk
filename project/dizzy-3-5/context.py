class Context:
    def __init__(self):
        self.lifes = 3
        self.score = 0
        self.room = "the entrance"
        self.map = None
        self.actors = []
        self.view_offset_x = 32
        self.view_offset_y = 0