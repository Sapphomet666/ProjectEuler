monthLengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthLengthsLY = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapyear(year):
    if year % 4 != 0:
        return False
    if year % 400 == 0:
        return False
    else:
        return True

day1 = 2 #0 is sunday
firstSundaysCount = 0
for year in range(1901, 2001):
    if isLeapyear(year):
        months = monthLengthsLY
    else:
        months = monthLengths
    #print(day1)
    for i in range(0, 12):
        print("month: " + str(i))
        print("day: " + str(day1))
        print("num first sundays: " + str(firstSundaysCount))
        print(" ")
        if day1 == 0:
            firstSundaysCount = firstSundaysCount + 1
        day1 = (day1 + months[i]) % 7

print(firstSundaysCount)