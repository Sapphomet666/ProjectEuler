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


def pFactorizationList(number, primeList):
    factorization = []
    for i in primeList:
        power = 0
        while number % i == 0:
            power += 1
            number = number // i
        factorization.append(power)
    return factorization

def scalarProduct(vector, scalar):
    prod = []
    for i in range(0, len(vector)):
        prod.append(vector[i] * scalar)
    return prod

primes = primees(100)

factoList = []
for i in range(2, 100 +1):
    for j in range(2, 100 +1):
        if scalarProduct(pFactorizationList(i, primes), j) not in factoList:
            factoList.append(scalarProduct(pFactorizationList(i, primes), j))
print(factoList)
print(len(factoList))