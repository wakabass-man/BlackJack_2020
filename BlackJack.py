from tkinter import *
from tkinter import font
from winsound import *
from Card import *
from Player import *
import random
class BlackJack:
    def __init__(self):
        self.window = Tk()
        self.window.title("Black Jack")
        self.window.geometry("800x600")
        self.window.configure(bg="green")
        self.fontstyle = font.Font(self.window, size=24, weight='bold', family='Consolas')
        self.fontstyle2 = font.Font(self.window, size=16, weight='bold', family='Consolas')
        self.player = Player("player")
        self.dealer = Player("dealer")
        self.betMoney = 0
        self.playerMoney = 1000
        self.LcardsPlayer = []
        self.LcardsDealer = []
        self.deckN = 0
        self.setupButton()
        self.setupLabel()
        self.window.mainloop()
    def setupButton(self):
        self.B50 = Button(self.window, text="Bet 50", width=6, height=1, font=self.fontstyle2, \
                          command=lambda X=50: self.pressedB(X))
        self.B50.place(x=50, y=500)
        self.B10 = Button(self.window, text="Bet 10", width=6, height=1, font=self.fontstyle2, \
                          command=lambda X=10: self.pressedB(X))
        self.B10.place(x=150, y=500)
        self.B1 = Button(self.window, text="Bet 1", width=6, height=1, font=self.fontstyle2, \
                         command=lambda X=1: self.pressedB(X))
        self.B1.place(x=250, y=500)
        self.Hit = Button(self.window, text="Hit", width=6, height=1, font=self.fontstyle2, command=self.pressedHit)
        self.Hit.place(x=400, y=500)
        self.Stay = Button(self.window, text="Stay", width=6, height=1, font=self.fontstyle2, command=self.pressedStay)
        self.Stay.place(x=500, y=500)
        self.Deal = Button(self.window, text="Deal", width=6, height=1, font=self.fontstyle2, command=self.pressedDeal)
        self.Deal.place(x=600, y=500)
        self.Again = Button(self.window, text="Again", width=6, height=1, font=self.fontstyle2,
                            command=self.pressedAgain)
        self.Again.place(x=700, y=500)
        self.Hit['state'] = 'disabled'
        self.Hit['bg'] = 'gray'
        self.Stay['state'] = 'disabled'
        self.Stay['bg'] = 'gray'
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'
    def setupLabel(self):
        self.LbetMoney = Label(text="$0", width=4, height=1, font=self.fontstyle, bg="green", fg="cyan")
        self.LbetMoney.place(x=200, y=450)
        self.LplayerMoney = Label(text="You have $1000", width=15, height=1, font=self.fontstyle, bg="green", fg="cyan")
        self.LplayerMoney.place(x=500, y=450)
        self.LplayerPts = Label(text="", width=2, height=1, font=self.fontstyle2, bg="green", fg="white")
        self.LplayerPts.place(x=300, y=300)
        self.LdealerPts = Label(text="", width=2, height=1, font=self.fontstyle2, bg="green", fg="white")
        self.LdealerPts.place(x=300, y=100)
        self.Lstatus = Label(text="", width=15, height=1, font=self.fontstyle, bg="green", fg="white")
        self.Lstatus.place(x=500, y=300)
    def pressedB(self, X):
        self.betMoney += X
        if self.betMoney <= self.playerMoney:
            self.LbetMoney.configure(text="$" + str(self.betMoney))
            self.playerMoney -= X
            self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney -= X
    def pressedDeal(self):
        self.player.reset()
        self.dealer.reset()
        self.cardDeck = [i for i in range(52)]
        random.shuffle(self.cardDeck)
        self.deckN = 0
        self.hitPlayer(self.player.inHand())
        self.hitDealerDown(self.dealer.inHand())
        self.hitPlayer(self.player.inHand())
        self.hitDealer(self.dealer.inHand())
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.B50['state'] = 'disabled'
        self.B50['bg'] = 'gray'
        self.B10['state'] = 'disabled'
        self.B10['bg'] = 'gray'
        self.B1['state'] = 'disabled'
        self.B1['bg'] = 'gray'
        self.Hit['state'] = 'active'
        self.Hit['bg'] = 'white'
        self.Stay['state'] = 'active'
        self.Stay['bg'] = 'white'
    def hitPlayer(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player.addCard(newCard)
        p = PhotoImage(file="cards/" + newCard.filename())
        self.LcardsPlayer.append(Label(self.window, image=p))
        self.LcardsPlayer[self.player.inHand() - 1].image = p
        self.LcardsPlayer[self.player.inHand() - 1].place(x=250 + n * 30, y=350)
        self.LplayerPts.configure(text=str(self.player.value()))
        PlaySound('sounds/cardFlip1.wav', SND_FILENAME)
    def hitDealerDown(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.dealer.addCard(newCard)
        p = PhotoImage(file="cards/b2fv.png")
        self.LcardsDealer.append(Label(self.window, image=p))
        self.LcardsDealer[self.dealer.inHand() - 1].image = p
        self.LcardsDealer[self.dealer.inHand() - 1].place(x=250 + n * 30, y=150)
        PlaySound('sounds/cardFlip1.wav', SND_FILENAME)
    def hitDealer(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.dealer.addCard(newCard)
        p = PhotoImage(file="cards/" + newCard.filename())
        self.LcardsDealer.append(Label(self.window, image=p))
        self.LcardsDealer[self.dealer.inHand() - 1].image = p
        self.LcardsDealer[self.dealer.inHand() - 1].place(x=250 + n * 30, y=150)
        PlaySound('sounds/cardFlip1.wav', SND_FILENAME)
    def pressedHit(self):
        self.hitPlayer(self.player.inHand())
        if self.dealer.value() < 17:
            self.hitDealer(self.dealer.inHand())
        if self.player.value() > 21:
            while self.dealer.value() < 17:
                self.hitDealer(self.dealer.inHand())
            self.checkWinner()
    def pressedStay(self):
        while self.dealer.value() < 17:
            self.hitDealer(self.dealer.inHand())
        self.checkWinner()
    def pressedAgain(self):
        PlaySound('sounds/ding.wav', SND_FILENAME)
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'
        self.B50['state'] = 'active'
        self.B50['bg'] = 'white'
        self.B10['state'] = 'active'
        self.B10['bg'] = 'white'
        self.B1['state'] = 'active'
        self.B1['bg'] = 'white'
        for l in self.LcardsPlayer:
            l.destroy()
        for l in self.LcardsDealer:
            l.destroy()
        self.LcardsPlayer = []
        self.LcardsDealer = []
        self.betMoney = 0
        self.LplayerPts["text"] = ""
        self.LdealerPts["text"] = ""
        self.Lstatus["text"] = ""
    def checkWinner(self):
        p = PhotoImage(file="cards/" + self.dealer.cards[0].filename())
        self.LcardsDealer[0].configure(image=p)
        self.LcardsDealer[0].image = p
        self.LdealerPts.configure(text=str(self.dealer.value()))
        if self.player.value() > 21:
            if self.dealer.value() > 21:
                self.Lstatus.configure(text="Push")
                self.playerMoney += self.betMoney
            else:
                self.Lstatus.configure(text="Player Busts")
                PlaySound('sounds/wrong.wav', SND_FILENAME)
        elif self.dealer.value() > 21:
            self.Lstatus.configure(text="Dealer Busts")
            self.playerMoney += self.betMoney * 2
            PlaySound('sounds/win.wav', SND_FILENAME)
        elif self.dealer.value() == self.player.value():
            self.Lstatus.configure(text="Push")
            self.playerMoney += self.betMoney
        elif self.dealer.value() < self.player.value():
            self.Lstatus.configure(text="You won!!")
            self.playerMoney += self.betMoney * 2
            PlaySound('sounds/win.wav', SND_FILENAME)
        else:
            self.Lstatus.configure(text="Sorry you lost!")
            PlaySound('sounds/wrong.wav', SND_FILENAME)
        self.betMoney = 0
        self.LplayerMoney.configure(text="Youhave$" + str(self.playerMoney))
        self.LbetMoney.configure(text="$" + str(self.betMoney))
        self.B50['state'] = 'disabled'
        self.B50['bg'] = 'gray'
        self.B10['state'] = 'disabled'
        self.B10['bg'] = 'gray'
        self.B1['state'] = 'disabled'
        self.B1['bg'] = 'gray'
        self.Hit['state'] = 'disabled'
        self.Hit['bg'] = 'gray'
        self.Stay['state'] = 'disabled'
        self.Stay['bg'] = 'gray'
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'active'
        self.Again['bg'] = 'white'
BlackJack()