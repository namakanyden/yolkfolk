from AnimatedActor import AnimatedActor
from ActorState import ActorStanding
from pgzero import game
from time import time

class DizzyActor(AnimatedActor):
    def __init__(self, *args, **kwargs):
        super().__init__('dizzy', sprite=(20, 20), duration=400, pingpong=True)
        self.state = ActorStanding(self)


    def update(self, key):
        print("+++++update")
        print(key)
        print(self.state.__str__())
        self.state.update(key)
