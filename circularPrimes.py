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


def rotations(list):
    rots = [list]
    for i in range(1, len(list)):
        #print(rots)
        rotsEnd = rots[-1]
        #print(rotsEnd)
        rots.append([rotsEnd[-1]] + rotsEnd[:-1])
    return rots


def int2List(number):
    numStr = str(number)
    list = []
    for i in numStr:
        list.append(int(i))
    return list


def circularFinder(list, primeList):
    circNums = []
    for i in range(0, len(list)):
        #print(i)
        element = list[i]
        index = 1
        circular = True
        j = [element[-1]] + element[:-1]
        while index < len(element) and circular:
            if j not in list:
                circular = False
            j = [j[-1]] + j[:-1]
            index += 1
        if circular:
            circNums.append(primeList[i])
    return(circNums)


def circularTrimmer(primeList):
    evenDigits = [0, 2, 4, 6, 8]
    list = [2, 3, 5, 7]
    for element in primeList[4:]:
        number = element
        hasEvenDigit = False
        while number >= 10:
            if number % 10 in evenDigits:
                hasEvenDigit = True
            number = number // 10
            if number in evenDigits:
                hasEvenDigit = True
        if not hasEvenDigit:
            list.append(element)
    return list


primeList = primees(1000000)
primeNoEvenDigi = circularTrimmer(primeList)
x = [int2List(y) for y in primeNoEvenDigi]
print(circularFinder(x, primeNoEvenDigi))
print(len(circularFinder(x, primeNoEvenDigi)))


#circList = isCircular(primeList)

#print(circList.count(True))
