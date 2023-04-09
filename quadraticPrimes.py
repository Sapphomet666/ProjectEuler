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


def polynomialEval(polynomial, number):
    total = 0
    exp = 1
    for i in range(0, len(polynomial)):
       total += polynomial[i] * exp
       exp = exp * number
    return total


def conseqPolyPrimes(polynomial, primeList):
    compositeFound = False
    index = 0
    while not compositeFound:
        if polynomialEval(polynomial, index) in primeList:
            index += 1
        else:
            compositeFound = True
            return index


polynom = [41, 1, 1]
primeList = primees(10000)
smallPrimes = []
while primeList[len(smallPrimes)] < 1000:
    smallPrimes.append(primeList[len(smallPrimes)])
#print(polynomialEval(polynom, 3))
#print(conseqPolyPrimes(polynom, primeList))

maxConsPrimes = 0
maxPoint = []
for i in smallPrimes:
    for j in range(-1000, 1001):
        if conseqPolyPrimes([i, j, 1], primeList) > maxConsPrimes:
            maxConsPrimes = conseqPolyPrimes([i, j,  1], primeList)
            maxPoint = [i, j]

print(maxConsPrimes)
print(maxPoint)
print(maxPoint[0]*maxPoint[1])
