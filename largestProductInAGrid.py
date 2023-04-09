def maxProd(numDigits,pLength):
    #numStr=str(number)
    #numDigits=[int(x) for x in numStr]
    if pLength > len(numDigits):
        return 0
    critPoints=[0, len(numDigits)-pLength]
    critVals=[]
    for i in range(1,len(numDigits)-pLength-1):
        if numDigits[i-1] <= numDigits[i-1+pLength] and numDigits[i+pLength] <= numDigits[i]:
            critPoints.append(i)
    for i in critPoints:
        a = 1
        for j in range(i, i+pLength):
            a=a*numDigits[j]
        critVals.append(a)
    return max(critVals)
#print(critPoints)
#print(critVals)
#print(max(critVals))
#print(maxProd(12,3))

def listToInt(list):
    integer = 0
    for i in range(0, len(list)):
        intStr=str(list[i])
        integer = integer * pow(10, len(intStr)) + list[i]
    return integer

def transpose(matrix):
    transpose = []
    for i in range(0, len(matrix[1])):
        row = []
        for j in range(0, len(matrix)):
            row.append(matrix[j][i])
        transpose.append(row)
    return transpose


def twoDMaxProd(matrix,pLength):
    critVals = []
    transposed = transpose(matrix)

    for i in range(0, len(matrix)):
        critVals.append(maxProd(matrix[i], pLength))
        rightDiag = []
        for j in range(0, min(len(matrix)-i, len(transposed))):
            rightDiag.append(matrix[i+j][j])
        critVals.append(maxProd(rightDiag, pLength))
        leftDiag = []
        for j in range(0, min(i+1, len(transposed))):
            leftDiag.append(matrix[i-j][j])
        critVals.append(maxProd(leftDiag, pLength))
        bRightDiag = []
        for j in range(0, min(len(matrix)-i, len(transposed))):
            rightDiag.append(matrix[i+j][len(transposed)-j-1])
        critVals.append(maxProd(bRightDiag, pLength))
        bLeftDiag = []
        for j in range(0, min(i+1, len(transposed))):
            leftDiag.append(matrix[i-j][len(transposed)-j-1])
        critVals.append(maxProd(bLeftDiag, pLength))

    for i in range(0, len(transposed)):
        critVals.append(maxProd(transposed[i], pLength))

    return max(critVals)

def matrixReader():
    mat = []
    f = open("c:/Users/18285/Downloads/minimal=11.txt")
    X = f.readlines()
    H = []
    K = []
    for i in range(0,len(X)):
        row = []
        H.append(X[i].split())
        for j in H[i]:
            if j.isdigit():
                row.append(j)
        if row != []:
          K.append(row)
    for i in range(0, len(K)):
        for j in range(0, len(K[i])):
            K[i][j] = int(K[i][j])
    return K

    return mat
matrix = matrixReader()
s = twoDMaxProd(matrix, 4)
print(s)
#mat = [[0, 0, 2], [1, 1, 0], [1, 1, 0]]
#print(listToInt(mat[0]))
#print(twoDMaxProd(mat, 2))
#for i in range(0,len(mat)):
    #print(mat[i])
#print(transpose(mat))
