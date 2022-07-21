from Cheater import Cheater
from Player import Player

import random

import matplotlib.pyplot as plt
import numpy as np


size = 1000
freq_player = 0.5

def random_start():
    temp = []
    for i in range(size):
        if(random.random() < freq_player):
            temp.append(Player(i))
        else:
            temp.append(Cheater(i))

    return temp

def clean_start():
    temp = []
    for i in range(size):
         temp.append(Player(i))

    return temp

def dirty_start():
    temp = []
    for i in range(size):
         temp.append(Cheater(i))

    return temp


def main():
    # p = Player(1)
    # p.info()

    # c = Cheater(2)
    # c.info()

    players = []
    player_id = []
    num_heads = []

    players = dirty_start()

    for i in range(size):
        for p in players:
            p.flip(random)

    for p in players:
            player_id.append(p.ID)
            num_heads.append(p.heads)


    freq = [num_heads.count(i) for i in range(size+1)]

    fig = plt.figure(figsize = (20, 10))
    plt.bar(range(size+1), freq, color = "green", align="center")
    plt.xlabel("Number of Heads")
    plt.ylabel("Frequency")
    plt.show()

if __name__ == '__main__':
    main()