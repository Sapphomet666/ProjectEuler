def complexProduct(complexA, complexB):
    realPart = (complexA[0] * complexB[0]) - (complexA[1] * complexB[1])
    imaginaryPart = (complexA[1] * complexB[0]) + (complexA[0] * complexB[1])
    return [realPart, imaginaryPart]


def vectorSum(vectorA, vectorB):
    total = []
    for i in range(0, len(vectorA)):
        total.append([])
        total[i] = vectorA[i] + vectorB[i]
    return total


def absoluteValue(integer):
    if integer > 0:
        return integer
    return -1 * integer

squarelength = 1001

matrix = []
row = []
for i in range(0, squarelength):
    matrix.append([])
for i in range(0, squarelength):
    for j in range(0, squarelength):
        matrix[i].append(0)


location = [squarelength // 2, squarelength // 2]
direction = [0, 1]
magnitude = 1
progress = 0
for i in range(0, squarelength * squarelength):

    matrix[location[0]][location[1]] = i + 1

    location = vectorSum(direction, location)

    progress += 1
    if progress == magnitude:
        progress = 0
        if direction[1] == 0:
            magnitude += 1
        direction = complexProduct(direction, [0, -1])

diagTotal = 0
for i in range(0, len(matrix)):
    for j in range(0, len(matrix)):
        if absoluteValue(i - (squarelength // 2)) == absoluteValue(j - (squarelength // 2)):
            diagTotal += matrix[i][j]
print(diagTotal)