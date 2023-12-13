"""
Module which contains all of the tiles used for Yahtzee.
"""


class Tile:
    """
    Base class for   Yahtzee tiles.
    """

    def __init__(self, name):
        """
        Initializes the tile.
        """
        self.name = name
        self.score = 0
        self.has_score = False

    def __str__(self):
        return self.name

    def finalize_score(self, value):
        """
        Scores tile and then locks it.
        """
        self.score = value
        self.has_score = True


class SumTile(Tile):
    """
    Tile in which all numbers are added up to create the score.
    """

    def __init__(self, name, number):
        """
        Initializes the tile.
        """
        super().__init__(name)
        self.number = number

    def score_tile(self, dice):
        """
        Scores the tile.
        """
        if not self.has_score:
            new_score = self.score
            if self.number == 0:
                new_score = sum(dice)
            else:
                for die in dice:
                    if die == self.number:
                        new_score += die
            return new_score
        return self.score


class NumberTile(Tile):
    """
    Tiles which check for more than 3 of a number.
    """

    def __init__(self, name, number_of):
        super().__init__(name)
        self.number_of = number_of

    def score_tile(self, dice):
        """
        Scores tile.
        """
        if not self.has_score:
            dice.sort()
            for index in range(len(dice) - self.number_of + 1):
                if len(set(dice[index : index + self.number_of])) == 1:
                    if len(set(dice)) == 1 and self.number_of == 5:
                        return 50
                    return sum(dice)
            return 0
        return self.score


class FullHouse(Tile):
    """
    Full house tile.
    """

    def __init__(self):
        """
        Initializes tile.
        """
        super().__init__(name="full house")

    def score_tile(self, dice):
        """
        Scores the tile.
        """
        if not self.has_score:
            dice.sort()
            if (len(set(dice)) == 2) and (
                dice.count(dice[0]) == 3 or dice.count(dice[0]) == 2
            ):
                return 25
            return 0
        return self.score


class SmallStraight(Tile):
    """
    Small straight tile.
    """

    def __init__(self):
        """
        Initializes tile.
        """
        super().__init__(name="small straight")

    def score_tile(self, dice):
        """
        Scores the tile.
        """
        if not self.has_score:
            dice = list(set(dice))
            dice.sort()
            if len(dice) >= 4 and (
                dice[:4] == [1, 2, 3, 4]
                or dice[:4] == [2, 3, 4, 5]
                or dice[1:] == [3, 4, 5, 6]
                or dice[:4] == [3, 4, 5, 6]
            ):
                return 30
            return 0
        return self.score


class LargeStraight(Tile):
    """
    Large straight tile.
    """

    def __init__(self):
        """
        Initializes tile.
        """
        super().__init__(name="large straight")

    def score_tile(self, dice):
        """
        Scores the tile.
        """
        if not self.has_score:
            dice.sort()
            if dice in ([1, 2, 3, 4, 5], [2, 3, 4, 5, 6]):
                return 40
            return 0
        return self.score
