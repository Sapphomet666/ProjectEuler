def collatzRoots(number):
    roots = []
    roots.append(2 * number)
    if number % 6 == 4:
        roots.append((number - 1) // 3)
    return roots

def searcher(data):
    foundNums = data[0] #a list of booleans corresponding to whether the index has been found or not
    numberFound = data[1] #the number of numbers below 1000000 that we've found
    distances = data[2] #a list containing 2 other lists representing the set of numbers we have found and how far away from 1 they are
    currentNums = data[3] #the set of numbers we're currently on with currentNums[0] representing their distance from 1

    row = [currentNums[0] + 1]
    for i in currentNums[1:]:
        for j in collatzRoots(i):
            row.append(j)
            if j < 1000000 and foundNums[j] == False:
                numberFound = numberFound + 1
                foundNums[j] = True
    distances.append(row)
    currentNums = row
    data = [foundNums, numberFound, distances, currentNums]
    if numberFound < 100000:
        data = searcher(data)

    return data

foundN = []
for i in range(0, 1000000):
    foundN.append(False)
foundN[1] = foundN[2] = foundN[4] = True
numberFound = 3
distances = [[0, 1], [1, 2], [2, 4]]
currentNum = [2, 4]
data = [foundN, numberFound, distances, currentNum]
x = searcher(data)
print(x[3])


