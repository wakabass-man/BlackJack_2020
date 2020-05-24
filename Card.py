class Card:
    def __init__(self, temp):
        self.value = temp % 13 + 1 #카드넘버
        self.x = temp//13 #카드무늬
    def getValue(self):#?
        if self.value > 10:
            return 10
        elif self.value == 1:
            return 11
        else:
            return self.value
    def getsuit(self):
        if self.x == 0:
            self.suit = "Clubs"
        elif self.x == 1:
            self.suit = "Spades"
        elif self.x == 2:
            self.suit = "Hearts"
        else:
            self.suit = "Diamonds"
        return self.suit
    def filename(self):
        return self.getsuit()+str(self.value)+".png"