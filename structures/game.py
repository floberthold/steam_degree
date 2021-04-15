class Game:
    def __init__(self, time, name):
        self.time = time
        self.name = name

    def as_credits(self):
        return self.time / 30
