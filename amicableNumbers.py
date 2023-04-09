def primees(bound):
    primeList = []
    isPrimeList = []
    for i in range(0, bound):
        isPrimeList.append(True)
    isPrimeList[0] = isPrimeList[1] = False
    for i in range(0, bound):
        if isPrimeList[i]:
            for j in range(2*i, bound, i):
                isPrimeList[j] = False
            primeList.append(i)

    return(primeList)


def listOfPFactors(number, primeList):
    factors = []
    for i in primeList:
        factors.append(0)
    i = 0
    while i < len(primeList):
        if number % primeList[i] == 0:
            factors[i] = factors[i] + 1
            number = number // primeList[i]
        else:
            i = i + 1
    return factors


def sumOfFactors(number, primeList):
    factors = listOfPFactors(number, primeList)
    total = 1
    for i in range(0, len(primeList)):
        total = total * ((pow(primeList[i], factors[i] + 1) - 1) // (primeList[i] - 1))
    return total - number


def isAmicable(number, primeList):
    if sumOfFactors(sumOfFactors(number, primeList), primeList) == number and sumOfFactors(number, primeList) != number:
        return True
    else:
        return False


def amicableList(bound, primeList):
    amiList = []
    facSums = [-1, 0]
    for i in range(2, bound):
        facSums.append(sumOfFactors(i, primeList))
    for i in range(2, bound):
        if facSums[i] >= bound:
            if i == sumOfFactors(facSums[i], primeList):
                amiList.append(i)
        else:
            if i != facSums[i] and i == facSums[facSums[i]]:
                amiList.append(i)
    return(amiList)


primes = primees(100000)
s = amicableList(10000, primes)
print(s)
print(sum(s))