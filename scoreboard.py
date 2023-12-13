"""
This is the module which contains scoreboard information.
"""

import tiles as t


all_tiles = [
    t.SumTile("ones", 1),
    t.SumTile("twos", 2),
    t.SumTile("threes", 3),
    t.SumTile("fours", 4),
    t.SumTile("fives", 5),
    t.SumTile("sixes", 6),
    t.NumberTile("three of a kind", 3),
    t.NumberTile("four of a kind", 4),
    t.FullHouse(),
    t.SmallStraight(),
    t.LargeStraight(),
    t.NumberTile("yahtzee", 5),
    t.SumTile("chance", 0),
]


class Scoreboard:
    """
    Representation of the game's scoreboard.
    """

    def __init__(self, contents):
        """
        Initializes scoreboard.
        """
        self.contents = contents
        self.total_score = 0

    def get_score(self, ind, die_list):
        """
        Gets the score of a tile at a certain index.
        """
        s = self.contents[ind].score_tile(die_list)
        return s

    def view_score(self, num, lst):
        """
        Views the score of a tile.
        """
        score = self.get_score(num, lst)
        print(f"{self.contents[num].name}: {score}")

    def lock_score(self, num, lst):
        """
        Locks the score for a tile and adds it to both the tile and board.
        """
        s = self.get_score(self.contents[num], lst)
        self.contents[num].score = s
        self.contents[num].hasScore = True
        self.total_score += s


sb = Scoreboard(all_tiles)
dice = [1, 2, 3, 4, 5]
count = 0
for t in sb.contents:
    sb.view_score(count, dice)
    count += 1
