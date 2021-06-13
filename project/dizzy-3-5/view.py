from movement import Movement

class View:
    def __init__(self, context, left, top, width, height):
        self.context = context
        self.left = left  # tile x
        self.top = top  # tile y
        self.width = width  # width in tiles
        self.height = height  # width in tiles

    # TODO zamysliet sa nad nazvom: view.contains_actor(actor)
    # TODO actor in view
    def is_actor_visible(self, actor):
        return (
                self.left * self.context.map.tilewidth
                <= actor.left
                <= (self.left + self.width) * self.context.map.tilewidth
                and self.top * self.context.map.tileheight
                <= actor.top
                <= (self.top + self.height) * self.context.map.tileheight
        )

    def move_view(self, view_movement: int):
        if view_movement == Movement.RIGHT:
            if self.left + self.width < self.context.map.width:
                self.left += 1
        elif view_movement == Movement.LEFT:
            if self.left > 0:
                self.left -= 1
        elif view_movement == Movement.UP:
            if self.top > 0:
                self.top -= 1
        else:
            if self.top + self.height < self.context.map.height:
                self.top += 1