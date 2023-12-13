import pygame
import random
import accessible_output2.outputs.auto


o = accessible_output2.outputs.auto.Auto()


pygame.init()
display = pygame.display.set_mode((300, 300))


roll = pygame.mixer.Sound("sound\dice.wav")
unlock = pygame.mixer.Sound("sound\\unlock.wav")
lock = pygame.mixer.Sound("sound\lock.wav")
lockedDice = pygame.mixer.Sound("sound\lockedDice.wav")


class Die:

    def __init__(self):
        self.value = 1
        self.lock = False

    def roll(self):
        if not self.lock:
            self.value = random.randint(1, 6)

    def getText(self):
        return f"{self.value}"


class DiceBox:

    SoundAnnounceValues = ["sound", "voice", "both"]

    def __init__(self, numberOfDice=5):
        self.dice = []
        self.lockAnnounceSetting = "sound"
        self.numberOfDice = numberOfDice
        for i in range(self.numberOfDice):
            self.dice.append(Die())
        self.index = 0
        self.SIndex = -1

        self.score = 0
        self.scoreboard = {
            "ones": {
                "value": 0,
                "state": "free",
            },
            "twos": {
                "value": 0,
                "state": "free",
            },
            "threes": {
                "value": 0,
                "state": "free",
            },
            "fours": {
                "value": 0,
                "state": "free",
            },
            "fives": {
                "value": 0,
                "state": "free",
            },
            "sixes": {
                "value": 0,
                "state": "free",
            },
            "three of a kind": {
                "value": 0,
                "state": "free",
            },
            "four of a kind": {
                "value": 0,
                "state": "free",
            },
            "full house": {
                "value": 0,
                "state": "free",
            },
            "small straight": {
                "value": 0,
                "state": "free",
            },
            "large straight": {
                "value": 0,
                "state": "free",
            },
            "yahtzee": {
                "value": 0,
                "state": "free",
            },
            "chance": {
                "value": 0,
                "state": "free",
            },
        }

    def getAllDiceText(self):
        msg = ""
        for die in self.dice:
            if die.lock == True:
                msg += die.getText() + ", " + "locked. "
            else:
                msg += die.getText()+", "
        return msg

    def announceValue(self, ind):
        """
        Announces the value of an individual die.
        ind represents the index of the die.
        """
        if self.dice[ind].lock == False:
            o.speak(self.dice[ind].value, )
        else:
            if self.lockAnnounceSetting == "sound":
                lockedDice.play()
                o.speak(str(self.dice[ind].value), interrupt=True)
            elif self.lockAnnounceSetting == "voice":
                o.speak(str(self.dice[ind].value) +
                        "," + "locked.", interrupt=True)
            else:
                lockedDice.play()
                o.speak(str(self.dice[ind].value) +
                        "," + "locked.", interrupt=True)

    def getCurrentDiceText(self):
        return self.dice[self.index].getText()

    def rollDice(self):
        roll.play()
        for die in self.dice:
            die.roll()

    def changeAnnounceSetting(self, speak):
        index = DiceBox.SoundAnnounceValues.index(self.lockAnnounceSetting)
        index += 1
        if index == 3:
            index = 0
        self.lockAnnounceSetting = DiceBox.SoundAnnounceValues[index]
        if self.lockAnnounceSetting == "sound":
            lockedDice.play()
        elif self.lockAnnounceSetting == "voice":
            speak("voice")
        else:
            speak("both")
            lockedDice.play()

    def lockDie(self):
        lock.play()
        self.dice[self.index].lock = True

    def unlockDie(self):
        unlock.play()
        self.dice[self.index].lock = False

    def moveRight(self):
        self.index += 1
        if self.index == len(self.dice):
            self.index = 0
        self.announceValue(self.index)

    def moveLeft(self):
        self.index -= 1
        if self.index == -1:
            self.index = len(self.dice)-1
        self.announceValue(self.index)

    def getDiceValues(self):
        values = []
        for die in self.dice:
            values.append(die.value)
        return values

    def moveScoreboard(self):
        """
        Moves through the player's scorecard.
        """
        keyList = list(self.scoreboard.keys())
        self.SIndex += 1
        if self.SIndex == len(keyList):
            self.SIndex = 0
        tile = keyList[self.SIndex]
        selectedTile = self.scoreValues(tile)
        o.speak(f"{tile}: {selectedTile}")


