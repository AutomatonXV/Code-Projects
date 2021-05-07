from Player import Human, Machine

class Board:    
    def __init__(self):
        self.Board = dict()
        #
        """ self.Board[0] = [-1,-1,-1]
        self.Board[1] = [-1,1,0]
        self.Board[2] = [0,1,0] """
        
        for x in range(3):
            self.Board[x] = [0,0,0]
        
        self.Symbols = dict()
        self.Symbols[0] = "   "
        self.Symbols[-1] = " X "
        self.Symbols[1] = " O "

        self.P1 = None
        self.P2 = None
        self.TurnPlayer = self.P1
        self.WinningPlayer = None
        self.EndGame = None


    def NewGame(self, HumanPlayers):
        if HumanPlayers > 3 or HumanPlayers <= 0:
            return
        
        if HumanPlayers == 1:
            self.P1 = Human()
            self.P2 = Machine()
        else:
            self.P1 = Human()
            self.P2 = Human()

        self.P1.setToken(-1)
        self.P2.setToken(1)
        self.TurnPlayer = self.P1

    def copyBoard(self):
        NewGame = Board()
        NewGame.NewGame(1)
        for row,arr in self.Board.items():
            col = 0
            for symbol in arr:
                NewGame.overrideSquare(row,col,symbol)
                col += 1
        return NewGame

    def invertBoard(self):
        NewGame = Board()
        NewGame.NewGame(1)
        for row,arr in self.Board.items():
            col = 0
            for symbol in arr:
                inverted = 0
                if symbol == -1:
                    inverted = 1
                elif symbol == 1:
                    inverted = -1
                NewGame.overrideSquare(row,col,inverted)
                col += 1
        return NewGame

    def overrideSquare(self,row,col,Symbol):
        self.Board[row][col] = Symbol

    def getPossibleInputs(self):
        #get a dictionnary of allowed inputs to set square
        index = 1
        InputDict = dict()
        for row,arr in self.Board.items():
            col = 0
            #print(arr)
            for symbol in arr:
                #print(symbol)
                if symbol == 0:
                    InputDict[index] = [row,col]
                    index +=1
                col +=1
        #print(self.InputDict)
        return InputDict

    def toNext(self):
        #check if win condition reached
        Winner = self.getWinCondition()
        if Winner:
            plr = self.Symbols[Winner]
            #print()
            self.EndGame = plr + "has won!"
            self.WinningPlayer = plr
            return
        #check if tie
        InputDict = self.getPossibleInputs()
        if len(InputDict.keys()) == 0:
            self.EndGame = "Tie!"
            #print("Game is a tie!")
            return
        #to next player
        if self.TurnPlayer == self.P1:
            self.TurnPlayer = self.P2
            #print("Changed to "+self.Symbols[self.TurnPlayer.Symbol])
        else:
            self.TurnPlayer = self.P1
            #print(self.TurnPlayer.Symbol)
            #print("Changed to "+self.Symbols[self.TurnPlayer.Symbol])
        
        
        
    def setSquare(self,no,Symbol = False):
        player = self.TurnPlayer
        
        number = int(no)
        if number == False:
            return None
        if number <= 0 or number > 9:
            return None
        InputDict = self.getPossibleInputs()
        if number in InputDict.keys():
            arr = InputDict[number]
            row = arr[0]
            col = arr[1]
            self.Board[row][col] = player.Symbol
            if Symbol:
                self.Board[row][col] = Symbol
                WinState = self.getWinCondition()
            #print("Set :(",str(row),";",str(col),") to ",self.Symbols[player.Symbol]) 
            #self.toNext()
        else:
            self.EndGame = "Invalid Move"
            print("INVALID INPUT!")
    
    def checkHorizontal(self,symbol):
        #Go horizontal
        for row, arr in self.Board.items():
            failedMatch = False
            for i in arr:
                if i != symbol:
                    failedMatch = True
            #if failedMatch is false, that means this entire row is full of the same symbol, aka win condition.
            if failedMatch == False:
                self.EndGame = self.Symbols[symbol] + "has won due to horizontal line!"
                print("Win due to horizontal line")
                return symbol
        return None
    
    def checkVertical(self,symbol):
        RowCount = len(self.Board.keys())#first get the number of rows
        ColCount = len(self.Board[0])#next get the number of columns
        CurrentCol = 0
        for col in range(ColCount):
            failedMatch = False
            for row, arr in self.Board.items():
                if arr[CurrentCol] != symbol:
                    failedMatch = True
            CurrentCol +=1

            if failedMatch == False:
                self.EndGame = self.Symbols[symbol] + "has won due to vertical line!"
                print("Win due to Vertical line")
                return symbol
        return None
    
    def checkDiagonals(self,symbol):
        #Diagonal left side: 1,1;2,2;3,3. Diagonal Right side: 3,1;2,2;1,3
        #Diagonal Left
        RowCount = len(self.Board.keys())#first get the number of rows
        failedMatch = False
        for row in range(RowCount):
            
            currCol = row
            if self.Board[row][currCol] != symbol:
                failedMatch = True

        if failedMatch == False:
            print("Win due to Left diagonal")
            self.EndGame = self.Symbols[symbol] + "has won due to horizontal line!"
            return symbol    

        failedMatch = False
        for row in range(RowCount):
            currCol = RowCount - row - 1
            #print(row,currCol,self.Board[row][currCol],"\t",symbol,failedMatch)
            if self.Board[row][currCol] != symbol:
                failedMatch = True

        if failedMatch == False:
            print("Win due to Right diagonal")
            self.EndGame = self.Symbols[symbol] + "has won due to horizontal line!"
            return symbol
        return None

    def getWinCondition(self):
        Tokens = [-1,1]
        for symbol in Tokens:
            self.checkHorizontal(symbol)
            self.checkVertical(symbol)
            self.checkDiagonals(symbol)
            if self.EndGame:
                return symbol
        PossibleMoves = self.getPossibleInputs()
        if len(list(PossibleMoves.keys())) == 0:
            self.EndGame = "Tie! Nobody wins"
            return None
        
        return None  




    def getBoardStr(self,showPossibleInput = False):
        #InputDict = self.getPossibleInputs()
        FullStr = ""
        Row = "-------------"
        Index = 1
        for row,arr in self.Board.items():
            
            FullStr = FullStr + Row + "\n"
            FullStr = FullStr + "|"
            for input in arr:
                
                symbol = self.Symbols[input]
                if input == 0 and showPossibleInput:
                    symbol = ">"+str(Index)+"<"
                    Index+=1
                FullStr = FullStr + symbol + "|"
                
            FullStr = FullStr + "\n"
        return FullStr    

        

