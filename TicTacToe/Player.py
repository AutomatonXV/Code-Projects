import random

class Human:
    def __init__(self):
        self.Symbol = None
        self.isMachine = False

    def setToken(self,token):
        self.Symbol = token

class Machine:
    def __init__(self):
        self.Symbol = None
        self.isMachine= True

    def setToken(self,token):
        self.Symbol = token
    
    
        
    def takeAction(self, Board,possibleMoves, atRandom = False):
        Symbol = Board.TurnPlayer.Symbol
        if atRandom:
            moveKeys = list(possibleMoves.keys())
            low = moveKeys[0]
            maxim = moveKeys[len(moveKeys)-1]
            choice = random.randint(low,maxim)
            Board.setSquare(choice)
        else:
            #Now this is where the fun begins
            #make a new game for every possible move, and check if a state of win or tie has been achieved.
            #repeat above but from opponent's perspective, until someone won.
            AttackDepth = 0 #In how many moves can the AI finish off the game?
            DefendDepth = 0 #In how many moves can the opponent finish off the AI?

            def ChangeSymbol(Symbol):
                if Symbol == -1:
                    return 1
                else:
                    return -1

            def findBestPath(OriginalSymbol,Board):
                #first sweep through the entire board, find which position would give X the win
                #second, sweep through the entire board, find which position would give me the win
                #if neither of the above are true, then find the shortest path to win
                #print("Checking my endgames")
                PossibleInputs = list(Board.getPossibleInputs().keys())
                for move in PossibleInputs:
                    New = Board.copyBoard()
                    New.setSquare(move,OriginalSymbol)
                    #print(move, New.EndGame)
                    if New.EndGame:
                        return move

                #print("Checking opponent endgames")
                for move in PossibleInputs:
                    New = Board.invertBoard()
                    New.setSquare(move,OriginalSymbol)
                    #print(New.getBoardStr())
                    #print(move, New.EndGame)
                    if New.EndGame:
                        #print("Found opponent endgame")
                        return move
                
                """ #neither first nor second condition reached, play random
                print("Playing at random")
                RNGMove = PossibleInputs[random.randint(0,len(PossibleInputs)-1)]
                print(RNGMove)
                return RNGMove """

                #Neither first nor second condition reached, find an endgame within possible moves
                for move in PossibleInputs:
                    New = Board.copyBoard()
                    New.setSquare(move,OriginalSymbol)
                    return findBestPath(ChangeSymbol(OriginalSymbol),New)

            Move = findBestPath(Symbol,Board)
            Board.setSquare(Move)
            




    