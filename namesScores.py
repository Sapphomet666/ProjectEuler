alphaBetDict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26
}


def namesReader():
    f = open("c:/Users/18285/Downloads/p022_names.txt")
    x = f.readlines()
    x = x[0].split(",")
    for i in range(0, len(x)):
        x[i] = x[i].strip("\"")
    return x


def alphaComp(stringA, stringB):
    stringA = stringA.casefold()
    stringB = stringB.casefold()
    if stringA == stringB:
        return True
    for i in range(0, min(len(stringA), len(stringB))):
        if alphaBetDict.get(stringA[i]) < alphaBetDict.get(stringB[i]):
            return True
        if alphaBetDict.get(stringA[i]) > alphaBetDict.get(stringB[i]):
            return False
    if len(stringA) < len(stringB):
        return True
    return False


def sorter(list, comparisonFunction):
    if len(list) == 1:
        return list

    listA = list[:len(list) // 2]
    listB = list[len(list) // 2:]
    listA = sorter(listA, comparisonFunction)
    listB = sorter(listB, comparisonFunction)

    indexA = 0
    indexB = 0
    sortedList = []
    while indexA + indexB < len(list):
        if indexA == len(listA):
            sortedList.append(listB[indexB])
            indexB += 1
        if indexB == len(listB) and indexA < len(listA):
            sortedList.append(listA[indexA])
            indexA += 1
        if indexA < len(listA) and indexB < len(listB):
            if comparisonFunction(listA[indexA], listB[indexB]):
                sortedList.append(listA[indexA])
                indexA += 1
            else:
                sortedList.append(listB[indexB])
                indexB += 1

    return sortedList


def nameScore(string):
    string = string.casefold()
    total = 0
    for letter in string:
        total += alphaBetDict.get(letter)
    return total


namesList = namesReader()
sortedNames = sorter(namesList, alphaComp)

total = 0
for i in range(0, len(sortedNames)):
    total += (i+1) * nameScore(sortedNames[i])
print(total)
