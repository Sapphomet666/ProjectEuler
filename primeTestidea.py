#problem 51

def primeTest(number):
    isPrime=True
    i=2
    while i<pow(number+1,0.5) and isPrime==True:
        if number%i==0:
            isPrime=False
        i=i+1
    return isPrime

def primeFamily(numberz,size):
    numberStr=str(numberz)
    

c=0
familySize=8
j=3
while c==0:
    if primeTest(j):
        if primeFamily(j,familySize):
            c=j
    j=j+2
print(c)

