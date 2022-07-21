from Player import Player

class Cheater(Player):

    def __init__(self, id) -> None:
        super().__init__(id)
        self.Label = "Cheater"
        self.Weight = 0.75