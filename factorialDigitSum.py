def listToInt(list):
    integer = 0
    for i in range(0, len(list)):
        intStr = str(list[i])
        integer = integer * pow(10, len(intStr)) + list[i]
    return integer


def bigAddition(bigIntA, bigIntB):
    bigIntSum = []
    carry = 0

    for i in range(0, min(len(bigIntA), len(bigIntB))):
        if bigIntA[i] + bigIntB[i] + carry >= 10000000000:
            bigIntSum.append(bigIntA[i] + bigIntB[i] + carry - 10000000000)
            carry = 1
        else:
            bigIntSum.append(bigIntA[i] + bigIntB[i] + carry)
            carry = 0

    if carry == 1:
        if len(bigIntA) == len(bigIntB):
            bigIntSum.append(1)
        if len(bigIntA) > len(bigIntB):
            bigIntA[len(bigIntB)] = bigIntA[len(bigIntB)] + 1
        if len(bigIntA) < len(bigIntB):
            bigIntB[len(bigIntA)] = bigIntB[len(bigIntA)] + 1

    if len(bigIntA) > len(bigIntB):
        for i in range(len(bigIntB), len(bigIntA)):
            bigIntSum.append(bigIntA[i])
    if len(bigIntB) > len(bigIntA):
        for i in range(len(bigIntA), len(bigIntB)):
            bigIntSum.append(bigIntB[i])

    return bigIntSum


def bigProduct(bigIntA, IntB):
    total = [0]
    for i in range(0, IntB):
        total = bigAddition(total, bigIntA)
    return total


def bigFactorial(IntA):
    fac = [1]
    for i in range(1, IntA + 1):
        fac = bigProduct(fac, i)
    return fac


def digitSum(number):
    total = 0
    while number > 9:
        total = total + (number % 10)
        number = number // 10
    total = total + number
    return total


def bigDigitSum(bigInt):
    total = 0
    for j in bigInt:
        total = total + digitSum(j)
    return total

#print(bigFactorial(100)) #big int blocks are displayed in reverse order: [1, 32] represents 320000000001
print(bigDigitSum(bigFactorial(100)))

