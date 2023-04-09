def maxSumPath(triangle):
    tSum = [triangle[0]]
    for i in range(1, len(triangle)):
        row = [triangle[i][0]+tSum[i - 1][0]]
        for j in range(1, len(triangle[i])-1):
            row.append(triangle[i][j] + max(tSum[i-1][j], tSum[i-1][j-1]))
        row.append(triangle[i][-1] + tSum[i-1][-1])
        tSum.append(row)
    return row

def matrixReader():
    mat = []
    f = open("c:/Users/18285/Desktop/triangleforprob18.txt")
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

triangle = matrixReader()
print(max(maxSumPath(triangle)))