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
        if bigIntA[i] + bigIntB[i] + carry > 10000000000:
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


f = open("c:/Users/18285/Desktop/10 numbers prob 13.txt")
X = f.readlines()

for i in range(0, len(X)):
    X[i] = X[i].strip("\n")

bigInts = []
for i in range(0, len(X)):
    row = []
    while len(X[i]) > 10:
        number = X[i][-10:]
        row.append(int(number))
        X[i] = X[i][:-10]
    row.append(int(X[i]))
    bigInts.append(row)

total = []
for i in range(0, len(bigInts)):
    total = bigAddition(total, bigInts[i])
print(total)