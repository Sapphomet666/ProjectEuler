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

def isRightTruncatable(primeList):
    oneDigitPrimes = [2, 3, 5, 7]
    rightTruncatables = []
    for prime in primeList[4:]:
        candidate = prime // 10
        if candidate in oneDigitPrimes or candidate in rightTruncatables:
            rightTruncatables.append(prime)
    return rightTruncatables


def isLeftTruncatable(primeList):
    oneDigitPrimes = [2, 3, 5, 7]
    leftTruncatables = []
    for prime in primeList[4:]:
        numDigits = 10
        while 10 * numDigits < prime:
            numDigits = numDigits * 10
        candidate = prime % numDigits
        if candidate in oneDigitPrimes or candidate in leftTruncatables:
            leftTruncatables.append(prime)
    return leftTruncatables


def setIntersection(setA, setB):
    intersection = []
    for element in setA:
        if element in setB:
            intersection.append(element)
    return intersection

primeList = primees(1000000)

rightTruncs = isRightTruncatable(primeList)
leftTruncs = isLeftTruncatable(primeList)
doubleTruncs = setIntersection(rightTruncs, leftTruncs)
print(doubleTruncs)
print(sum(doubleTruncs))