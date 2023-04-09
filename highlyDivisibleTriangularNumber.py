def primees():
    primeList = [2]
    i = 3
    length = 1
    while length < 100:
        isPrime = True
        index = 0
        while isPrime and index < length:
            if i % primeList[index] == 0:
                isPrime = False
            index = index+1
        if isPrime:
            primeList.append(i)
            length = length+1
        i = i+2
    return(primeList)

def numOfFactors(number, primeList):
    factors = []
    for i in primeList:
        factors.append(1)
    i = 0
    while i < len(primeList):
        if number % primeList[i] == 0:
            factors[i] = factors[i] + 1
            number = number / primeList[i]
        else:
            i = i + 1
    prod = 1
    for i in range(0, len(factors)):
        prod = prod * factors[i]
    return prod

def triangleFacs(bound):
    triangle = [0]
    primes = primees()
    found = False
    i = 1
    while not found:
        triangle.append(triangle[i-1]+i)
        if numOfFactors(triangle[i], primes) < bound:
            i = i+1
        else:
            return triangle[i]
print(triangleFacs(1000))


