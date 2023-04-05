import pygame
import random
pygame.init()
display = pygame.display.set_mode((300, 300))


roll = pygame.mixer.Sound("sound\dice.wav")
unlock = pygame.mixer.Sound("sound\\unlock.wav")
lock = pygame.mixer.Sound("sound\lock.wav")
lockedDice = pygame.mixer.Sound("sound\lockedDice.wav")

class Die:
    def __init__(self):
        self.value = 1
        self.lock=False

    def roll(self):
        if not self.lock:
            self.value = random.randint(1, 6)

    def getText(self):  
        if self.lock:
            lockedDice.play()
            return f"{self.value}, locked,"
            
        return f"{self.value}"


class DiceBox:
    def __init__(self,numberOfDice=5):
        self.dice=[]
        self.numberOfDice=numberOfDice
        for i in range(self.numberOfDice):
            self.dice.append(Die())
            self.index =0
            self.score = 0
            self.scoreboard = {
                "ones": 0,
                "twos": 0,
                "threes": 0,
                "fours": 0,
                "fives": 0,
                "sixes": 0,
                "three of a kind": 0,
                "four of a kind": 0,
                "full house": 0,
                "small straight": 0,
                "large straight": 0,
                "yahtzee": 0,
                "chance": 0,
            }
            
    def getAllDiceText(self):
        msg = ""
        for die in self.dice:
            msg += die.getText()+" "
        return msg    

    def getCurrentDiceText(self):
        return  self.dice[self.index].getText()
        
    def rollDice(self):
        roll.play()
        for die in self.dice:
            die.roll()
        
    def lockDie(self):
        lock.play()
        self.dice[self.index].lock=True
        
    def unlockDie(self):
        unlock.play()
        self.dice[self.index].lock=False
        

    def moveRight(self):
        self.index+=1
        if self.index == len(self.dice): 
            self.index =0
        return self.dice[self.index].getText()

    def moveLeft(self):
        self.index-=1
        if self.index == -1: 
            self.index =len(self.dice)-1
        return self.dice[self.index].getText()

    def getDiceValues(self):    
        values=[]
        for die in self.dice:
            values.append(die.value)
        return values
                    
    def scoreDiceOf(self,side=0):
        """Add all the dice for score that are the given side value.  If 0 then add them all"""
        score=0
        for die in self.dice:
            if side == 0  or die.value == side:
                score+=die.value
        return score
       
    def scoreNumberOf(self,numberOf=3):
        """Scores three of a kind and four of a kind
        can be used for yahtzee
        """
        values=self.getDiceValues()
        values.sort()
        for index in range(len(values)-numberOf+1):
            if len(set(values[index:index+numberOf])) == 1:
                if len(set(values)) == 1:
                    return 50
                else:
                    return sum(values)
        return 0
              
    def scoreLarge(self):
        values=self.getDiceValues()
        values.sort()
        if values == [1,2,3,4,5] or values == [2,3,4,5,6]:
            return 40
        return 0
        
    def scoreSmall(self):
        values=self.getDiceValues()
        values=list(set(values))
        values.sort()
        if len(values)>=4 and (values[:4]== [1,2,3,4] or values[:4]==[2,3,4,5] or values [:4]==[3,4,5,6]):
            return 30
        return 0            

    def scoreFullHouse(self):
        values=self.getDiceValues()
        values.sort()
        if ((values [0] ==values[1] and values[1] != values [2] and values [2] ==values[3] ==values[4]) or
            (values[0]==values[1]==values[2] and values[2]!=values[3] and values [3]==values[4])):
            return 25
        return 0            
    
    def scoreValues(self, value):
        if value in self.scoreboard:
            if value == "ones":
                self.scoreDiceOf(1)
            elif value == "twos":
                self.scoreDiceOf(2)
            elif value == "threes":
                self.scoreDiceOf(3)
            elif value == "fours":
                self.scoreDiceOf(4)
            elif value == "fives":
                self.scoreDiceOf(5)
            elif value == "sixes":
                self.scoreDiceOf(6)
            elif value == "three of a kind":
                self.scoreNumberOf(3)
            elif value == "four of a kind":
                self.scoreNumberOf(4)
            elif value == "full house":
                self.scoreFullHouse()
            elif value == "small straight":
                self.scoreSmall()
            elif value == "large straight":
                self.scoreLarge()
            elif value == "yahtzee":
                self.scoreNumberOf(5)
            elif value == "chance":
                self.scoreDiceOf(0)
        else:
            print("Sorry, an error has occured.")

    
    
        
            
if __name__ == "__main__":
    d=DiceBox(5)
    d.rollDice()
    print(f"Test roll = {d.getAllDiceText()}")
    for i in range(7):
        print (f"Score {i}'s: {d.scoreDiceOf(i)}")
    print (f"Three of a kind {d.scoreNumberOf(3)}")
    print (f"Four  of a kind {d.scoreNumberOf(4)}")
    print (f"full house: {d.scoreFullHouse()}")
    print(f"small {d.scoreSmall()}")
    print(f"Large {d.scoreLarge()}")
    if d.scoreNumberOf(5) >0:
        print ("Yahtzee")
