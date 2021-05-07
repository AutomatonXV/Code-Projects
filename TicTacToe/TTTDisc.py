#For discord bots
#Call NewGame to start a game, and use NewInput and getBoardStr to play.

from Board import Board
#myGame = Board()
#myGame.NewGame(1) #Set this to 2 if you want a human vs human battle. But human v human is not implemented. Do it yourself!
print("Starting game against AI")

class TTTManager:
    def __init__(self):
        MyGame = None
        #SETUP

    def NewGame(self):
        self.MyGame = Board()
        self.MyGame.NewGame(1)
        self.MyGame.toNext()
        self.MyGame.setSquare(5)
        #self.MyGame.TurnPlayer.takeAction(self.MyGame,self.MyGame.getPossibleInputs(),True)
        self.MyGame.toNext()
        return self

    def NewInput(self,txt):

        self.MyGame.setSquare(txt)
        self.MyGame.toNext()
        if self.MyGame.EndGame:
            return self.MyGame.EndGame, self.MyGame.getBoardStr()

        self.MyGame.TurnPlayer.takeAction(self.MyGame,self.MyGame.getPossibleInputs(),False)
        self.MyGame.toNext()
        if self.MyGame.EndGame:
            return self.MyGame.EndGame, self.MyGame.getBoardStr()
        
        return self.MyGame.EndGame, self.MyGame.getBoardStr(True)
    

    def getBoardStr(self):
        return self.MyGame.getBoardStr(True)