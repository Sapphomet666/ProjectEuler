def powDigitCalculator(number, power):
    strNum = str(number)
    digiList = []
    for i in strNum:
        digiList.append(int(i))

    total = 0
    for i in digiList:
        total += pow(i, power)
    return total

selfPowSum = []

for i in range(2, 1000000):
    if i == powDigitCalculator(i, 5):
        selfPowSum.append(i)
print(sum(selfPowSum))