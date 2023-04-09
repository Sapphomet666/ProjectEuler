def factorial(number):
    prod = 1
    for i in range(1, number + 1):
        prod = prod * i
    return prod


def listToInt(list):
    integer = 0
    for i in range(0, len(list)):
        intStr = str(list[i])
        integer = integer * pow(10, len(intStr)) + list[i]
    return integer


bound = 10
lexNumber = 1000000 - 1
ordering = []

availableNums = []
for i in range(0, bound):
    availableNums.append(i)

for i in range(0, bound):
    ordering.append(availableNums[lexNumber // factorial(bound-i-1)])
    availableNums.pop(lexNumber // factorial(bound - i - 1))
    lexNumber = lexNumber % factorial(bound-i-1)

print(ordering)
print(listToInt(ordering))