primeList = [2]
i = 3
length = 1
while length < 10001:
    isPrime = True
    index = 0
    while isPrime and index < length:
        if i % primeList[index] == 0:
            isPrime = False
        index = index+1
    if isPrime:
        primeList.append(i)
        length = length+1
    i = i+2
print(primeList[10000])
