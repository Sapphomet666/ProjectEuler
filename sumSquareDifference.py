def sumOfSquares(n):
    tatl=0
    for i in range(1,n+1):
        tatl=tatl+pow(i,2)
    return tatl
def squareOfSum(n):
    tatl=0
    for i in range(1,n+1):
        tatl=tatl+i
    tatl=pow(tatl,2)
    return tatl
print(squareOfSum(100)-sumOfSquares(100))
