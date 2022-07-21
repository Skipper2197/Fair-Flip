class Player:

    def __init__(self, id) -> None:
        self.ID = id
        self.Label = "Player"
        self.Weight = 0.5

        self.heads = 0
        self.tails = 0

    def flip(self, r):
        if(r.random() < self.Weight):
            self.heads += 1
        else:
            self.tails += 1

    def info(self) -> str:
        print("Player {0} is a {1} and has a weight of {2}\t\t Heads: {3}\t Tails: {4}".format(self.ID, self.Label, self.Weight, self.heads, self.tails))