
class Voin:
    def __init__(self, hp: int):
        self.hp = hp

    def hit(self):
        self.hp = self.hp - 20
