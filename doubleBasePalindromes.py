def palindromes(maxDigits):
    palList = []
    numList = [1]
    if maxDigits % 2 == 1:
        evenMaxDigi = False
    else:
        evenMaxDigi = True
    leng = pow(10, (maxDigits) // 2)
    for i in range(1, pow(10, (maxDigits +1) // 2)):

        reverseCopy = numList.copy()
        reverseCopy.reverse()

        palList.append(reverseCopy + numList[1:])
        if evenMaxDigi or i < leng:
            palList.append(reverseCopy + numList)

        index = 0
        numList[0] += 1
        carried = -1
        while numList[index] == 10:
            if index < len(numList) - 1:
                numList[index+1] += 1
            else:
                numList.append(1)
            index += 1
        for j in range(0, len(numList)):
            if numList[j] == 10:
                numList[j] = 0

    return palList


def isBaseTwoPal(number):
    binary = bin(number)
    binary = binary[2:]
    for i in range(0, len(binary)//2):
        if binary[i] != binary[-i-1]:
            return False
    return True


def int2List(number):
    numStr = str(number)
    list = []
    for i in numStr:
        list.append(int(i))
    return list


def list2Int(list):
    number = 0
    for digit in list:
        number = number * 10
        number += digit
    return number

pal = palindromes(6)
palInts = [list2Int(x) for x in pal]

total = 0
multiBasePalindromes = []
for pali in palInts:
    if isBaseTwoPal(pali):
        multiBasePalindromes.append(pali)
        total += pali

print(total)
print(multiBasePalindromes)