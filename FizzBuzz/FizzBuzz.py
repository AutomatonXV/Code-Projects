class FizzBuzzSimple:
    def __init__(self, Fno = 3, Bno = 5):
        self.FizzNo = Fno
        self.BuzzNo = Bno

    def PlayFizzBuzz(self,iteration = 100):
        CompiledList = []                      #list of all fizz/buzz from 1 to iteration
        for i in range(1, iteration):
            OutputStr = ""

            if (i%self.FizzNo==0):             #Play fizz/buzz
                OutputStr += "Fizz"
            if (i%self.BuzzNo ==0):
                OutputStr += "Buzz"
            if not OutputStr:
                OutputStr = i

            CompiledList.append(OutputStr)     #add it to compiled list

        return CompiledList


