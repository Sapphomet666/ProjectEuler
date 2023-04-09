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

primes = primees(30000)

abundantList = []
for i in range(0, 28123):
    abundantList.append(False)
for i in range(2, 28123):
    if not abundantList[i] and sumOfFactors(i, primes) > i:
        for j in range(i, 28123, i):
            abundantList[i] = True

abundantNums = []
for i in range(0, len(abundantList)):
    if abundantList[i]:
        abundantNums.append(i)

isAbundantSum = []
for i in range(0, 28123):
    isAbundantSum.append(False)

for i in range(0, len(abundantNums)):
    for j in range(i, len(abundantNums)):
        if abundantNums[i] + abundantNums[j] < 28123:
            isAbundantSum[abundantNums[i] + abundantNums[j]] = True

total = 0
for i in range(0, 28123):
    if not isAbundantSum[i]:
        total += i

print(total)