
import random
import queue
import sys
class deck:
    
    def __init__(self):
        deck.data = queue.Queue(52)
        shufflearray = ["Ace","Ace","Ace","Ace","2","2","2","2","3","3","3","3",
                        "4","4","4","4","5","5","5","5","6","6","6","6","7"
                        ,"7","7","7","8","8","8","8","9","9","9","9","10","10"
                        ,"10","10","Jack","Jack","Jack","Jack","Queen","Queen"
                        ,"Queen","Queen","King","King","King","King"]
    
        for x in range(0, 20):
            for y in range(0, 52):
                randomNumber = random.randint(0, 51)
                firstSwap = shufflearray[y]
                secondSwap =  shufflearray[randomNumber]
                shufflearray[y] = secondSwap
                shufflearray[randomNumber] = firstSwap
        for x in shufflearray:
            deck.data.put(x)
    def get(self):
        return(deck.data.get())
  

class hand:
   
    def __init__(self):
        self.data = []        
    def addCard(self,x):
        self.data = self.data.append(x)
    def __repr__(self):
        return(str(self.data))
    def append(self, x):
        return self.data.append(x)
    def length(self):
        return(len(self.data))             
    def totalCount(self):
        totalCount = 0
        aceCount = 0
        acesCounted = 0
        for x in self.data:
            if x == "Queen" or x == "King" or x == "Jack":
                totalCount = totalCount + 10
            elif x == "1" or x == "2" or x == "3" or x == "4" or x == "5" or x =="6" or x == "7" or x == "8" or x == "9" or x == "10":
                totalCount = totalCount + int(x)
            else:
                if totalCount + 11 > 21:
                    totalCount = totalCount + 1
                else:
                    aceCount = aceCount + 1
                    totalCount = totalCount + 1
        if aceCount > 0 and totalCount <= 10:
            totalCount = totalCount + 10 #To account for aces being 11
            acesCounted = acesCounted + 1
        if acesCounted > 0 and totalCount > 21:
            totalCount = totalCount - 10
            acesCounted = acesCounted - 1
            
        return totalCount
    def checkEnd(self):
        totalCount = self.totalCount()  
        if totalCount == 21:
            return(True)
        elif totalCount > 21:
            return(False)
        else:
            return(totalCount)
        
    
class game:
    
    def __init__(self):
        print("Welcome to the casino! May luck be on your side!")
        game.data = True #True will be the player's turn, false is dealer's
    def gameOver(self, result):
        print(result)
        sys.exit(0)
    def passed(self):
        game.data = not game.data
        
            
game = game() 
inputted = input("New game? Yes or No")   
inputted = inputted.casefold()
inputted = inputted.strip()
if(inputted == "yes"):
    print("Game started!")
else:
    print("Ok, so you're scared eh? See you next time.")
    sys.exit(0)
           
deck = deck()
player = hand()
dealer = hand()
player.append(deck.get())
player.append(deck.get())
print("Player hand:" + str(player), "Total points:" + str(player.totalCount()))
dealer.append(deck.get())
print("Dealer hand:" + str(dealer), "Total points:" + str(dealer.totalCount()))
dealer.append(deck.get())## typical starting, player has 2 cards showing, dealer has 1 showing but has 2 in hand
while(game.data == True):
    x = input("Hit or Stand?")
    x = x.casefold()
    x = x.strip()
    if x == "hit":
        player.append(deck.get())
        print("Player hand:" + str(player), "Total points:" + str(player.totalCount()))
        if player.checkEnd() == True:
            game.gameOver("Player wins")
        elif player.checkEnd() == False:
            game.gameOver("Dealer wins")
    elif x == "stand":
        if player.checkEnd() == True:
            game.gameOver("Player wins")
        game.passed()
while(game.data == False):
        if dealer.totalCount() < 16:
            dealer.append(deck.get())
            #print("Dealer hand:" + str(dealer), "Total points:" + str(dealer.totalCount()))
            #if dealer.checkEnd() == False and player.checkEnd() != False :
                #game.gameOver("Player wins")
           # elif player.checkEnd() > dealer.checkEnd():
                #game.gameOver("Player wins")
           # else:
               # game.gameOver("Dealer wins")
        else:
            if dealer.checkEnd() == False and player.checkEnd() != False :
                print("Player hand:" + str(player), "Total points:" + str(player.totalCount()))
                print("Dealer hand:" + str(dealer), "Total points:" + str(dealer.totalCount()))
                game.gameOver("Player wins")
                
            elif player.checkEnd() > dealer.checkEnd():
                print("Player hand:" + str(player), "Total points:" + str(player.totalCount()))
                print("Dealer hand:" + str(dealer), "Total points:" + str(dealer.totalCount()))
                game.gameOver("Player wins")
                
            else:
                print("Player hand:" + str(player), "Total points:" + str(player.totalCount()))
                print("Dealer hand:" + str(dealer), "Total points:" + str(dealer.totalCount()))
                game.gameOver("Dealer wins")
            

            
        
            
            
    




