def factorial(number):
    prod = 1
    for i in range(1, number + 1):
        prod = prod * i
    return prod


def baseFactorial2Permutation(list):
    listCopy = list.copy()
    listCopy.pop()
    listCopy.reverse()
    listCopy.append(0)
    availableNums = []
    listLength = len(list)
    for i in range(0, listLength):
        availableNums.append(i+1)
    for i in range(0, listLength):
        j = availableNums[listCopy[i]]
        availableNums.pop(listCopy[i])
        listCopy[i] = j

    return listCopy


def permWriter(bound):
    perms = []
    row = []
    facBound = factorial(bound)
    for i in range(0, bound):
        row.append(0)
    for i in range(0, facBound):
        perms.append(row.copy())

    index = 0
    for i in range(0, facBound):
        perms[i][0] = index
        index += 1
        if index == 2:
            index = 0

    for i in range(1, bound):
        index = 0
        for j in range(0, facBound):
            perms[j][i] = index
            if perms[j][i-1] == i:
                increasePerm = True
                for k in range(0, i-1):
                    if perms[j][k] != k+1:
                        increasePerm = False
                if increasePerm:
                    index += 1

            if index == i + 2:
                index = 0

    for i in range(0, len(perms)):
        perms[i] = baseFactorial2Permutation(perms[i])

    return perms


def list2Int(list):
    int = 0
    for x in list:
        int += x
        int = 10 * int
    int = int // 10
    return int


def list2set(list):
    set = []
    for x in list:
        append = True
        for y in set:
            if x == y:
                append = False
        if append:
            set.append(x)

    return set


permutations = permWriter(9)

panDigiProducts = []
panDigiMultipliers = []
index = 0
while index < len(permutations):
    if list2Int(permutations[index][-2:]) * list2Int(permutations[index][-5:-2]) == list2Int(permutations[index][:-5]):
        if list2Int(permutations[index][-5:]) not in panDigiProducts:
            panDigiProducts.append(list2Int(permutations[index][:-5]))
            panDigiMultipliers.append([list2Int(permutations[index][-2:]), list2Int(permutations[index][-5:-2])])
        index += 1
    index += 1

index = 0
while index < len(permutations):
    if list2Int(permutations[index][-1:]) * list2Int(permutations[index][-5:-1]) == list2Int(permutations[index][:-5]):
        panDigiProducts.append(list2Int(permutations[index][:-5]))
        panDigiMultipliers.append([list2Int(permutations[index][-1:]), list2Int(permutations[index][-5:-1])])
        index += 1
    index += 1

print(sum(list2set(panDigiProducts)))
