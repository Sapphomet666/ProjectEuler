def repeatLengthReciprocal(a):
    integer = a
    while a % 2 == 0:
        a = a // 2
    while a % 5 == 0:
        a = a // 5
    if a == 1:
        return 0
    remaindersFound = []
    remainder = 1
    remaindersFound.append([remainder // integer, remainder])
    remainder = (10 * remainder) % integer
    while remaindersFound[-1] not in remaindersFound[:-1]:
        remaindersFound.append([remainder // integer, remainder])
        remainder = (10 * remainder) % integer
    index = remaindersFound.index(remaindersFound[-1])
    return len(remaindersFound) - index - 1

print(repeatLengthReciprocal(7))

maxLength = 0
maxLengthIndex = 0

for i in range(1, 1000):
    if repeatLengthReciprocal(i) > maxLength:
        maxLength = repeatLengthReciprocal(i)
        maxLengthIndex = i

print(maxLength)
print(maxLengthIndex)