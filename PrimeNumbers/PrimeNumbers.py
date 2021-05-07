class PrimeNumbersSimple:
    def __init__(self):
        pass

    def getPrimes(self,RangeMin=1, RangeMax=10000):
        Results = []
        if RangeMin < 0 or RangeMax < 0:
            raise Exception("Both boundaries must be positive.")
        if RangeMin >= RangeMax:
            raise Exception("Minimum number must be less than Maximum number.")

        for i in range(RangeMin,RangeMax):
            isPrime = True
            for n in range(2,i-1):
                if i%n == 0:
                    isPrime = False
                    break
            if isPrime:
                Results.append(i)

        return Results