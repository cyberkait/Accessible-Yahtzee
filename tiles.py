class Tile:
    """
    Base class for Yahtzee tiles.
    """
    def __init__(self, name):
        """
        Initializes the tile.
        """
        self.name = name
        self.score = 0
        self.hasScore = False
    def __str__(self):
        return self.name
    def finalize_score(self, value):
        """
        Scores tile and then locks it.
        """
        self.score = value
        self.hasScore = True


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
        if self.hasScore == False:
            new_score = self.score
            for die in dice:
                if die == self.number:
                    new_score += die
            return new_score


class NumberTile(Tile):
    """ 
    Tiles which check for more than 3 of a number.
    """ 
    def __init__(self, name, numberOf):
        super().__init__(name)
        self.numberOf = numberOf
    def score_tile(self, dice):
        """
        Scores tile.
        """
        if self.hasScore == False:
            dice.sort()
            for index in range(len(dice)-self.numberOf+1):
                if len(set(dice[index:index+self.numberOf])) == 1:
                    if len(set(dice)) == 1:
                        return 50
                    else:
                        return sum(dice)
            return 0


class FullHouse(Tile):
    """
    Full house tile.
    """
    def __init__(self):
        """
        Initializes tile.
        """
        super().__init__(name="full house")
        self.name = name
    def score_tile(self, dice):
        """
        Scores the tile.
        """
        if self.hasScore == False:
            dice.sort()
            if ((dice[0] == dice[1] and dice[1] != dice[2] and dice[2] == dice[3] == dice[4]) or
                (dice[0] == dice[1] == dice[2] and dice[2] != dice[3] and dice[3] == dice[4])):
                return 25
            return 0


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
        if self.hasScore == False:
            dice = list(set(dice))
            dice.sort()
            if len(dice) >= 4 and (dice[:4] == [1, 2, 3, 4] or dice[:4] == [2, 3, 4, 5] or dice[1:] == [3, 4, 5, 6]or dice[:4] == [3, 4, 5, 6] ):
                return 30
            return 0


class LargeStraight(Tile):
    """
    Large straight tile.
    """
    def __init__(self):
        """
        Initializes tile.
        """
        super().__init__(name="large straight")
        self.name = name
    def score_tile(self, dice):
        """
        Scores the tile.
        """
        if self.hasScore == False:
            dice.sort()
            if dice == [1, 2, 3, 4, 5] or dice == [2, 3, 4, 5, 6]:
                return 40
            return 0
