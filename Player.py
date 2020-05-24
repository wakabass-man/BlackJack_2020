#from Card import *
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.N = 0 #카드 갯수
        self.A = 0
    def addCard(self, c):
        self.cards.append(c)
        self.N += 1
        if c.getValue() == 11:
            self.A += 1
    def inHand(self):
        return self.N
    def reset(self):
        self.N = 0
        self.cards.clear()
        self.A = 0
    def value(self):
        cnt = self.A
        sum = 0
        for i in range(self.N):
                sum += self.cards[i].getValue()
        while sum > 21 and cnt > 0:
            sum -= 10
            cnt -= 1
        return sum