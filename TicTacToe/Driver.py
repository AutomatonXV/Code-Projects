from Board import Board
myGame = Board()
myGame.NewGame(1) #Set this to 2 if you want a human vs human battle. But human v human is not implemented. Do it yourself!
print("Starting game against AI")
print(myGame.getBoardStr(True))
Round = 0
while myGame.EndGame == None:
    myGame.toNext()
    print(myGame.getBoardStr(True))
    if myGame.EndGame != None:
        break
    #if machine, take action
    if myGame.TurnPlayer.isMachine:
        print("My turn.")
        myInputs = myGame.getPossibleInputs()
        if Round == 0:
            myGame.TurnPlayer.takeAction(myGame,myInputs,True) #First action at random
        else:
            #myGame.setSquare(4)
            myGame.TurnPlayer.takeAction(myGame,myInputs,False)
    else:
        print("Your move: "+myGame.Symbols[myGame.TurnPlayer.Symbol])
        myGame.setSquare(input("Input your choice, from 1 to 9."))
    Round +=1 


print(myGame.getBoardStr())
print(myGame.EndGame)
#print(myGame.Symbols[myGame.getWinCondition()]+ "has won!")